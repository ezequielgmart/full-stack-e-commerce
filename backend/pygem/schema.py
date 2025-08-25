from pygem.queries import Query

# Clase de una columna simple
class Column():
    def __init__(self, type, primary_key = False):
            
        self.type = type
        self.name = None # El nombre es inicialmente None
        self.primary_key = primary_key # El nombre es inicialmente None

# Esta clase será muy similar a tu Column, 
# pero incluirá una referencia a la tabla y la columna a la que se conecta.
class ForeignKey(Column): 

    def __init__(self, reference:str, **kwargs):
        super().__init__(kwargs)
        self.reference = reference
"""

Esta es la parte más avanzada. Esta clase no se mapea a una columna en la base de datos. 
Su única responsabilidad es guardar la información necesaria para que tu ORM pueda
 construir la consulta de relación.

Ahora metaclass detecta las relaciones, pero la lógica para que mi_producto.stock_info haga una consulta de SELECT y devuelva el objeto ProductStock es el siguiente desafío. Es un paso importante para darle a al ORM una verdadera funcionalidad de navegación.

La forma de lograrlo en Python es a través de un concepto llamado *DESCRIPTORES*. Un descriptor es un objeto que, cuando se accede como un atributo, se activa y ejecuta un código. Tu clase Relationship se convertirá en un descriptor.

Convertir Relationship en un descriptor

Se le agregara un método especial llamado __get__. Este método se llamará automáticamente cada vez que accedas a un atributo de relación, como mi_producto.inventory.

"""
class Relationship():
    def __init__(self, model, foreign_key_column, uselist:bool=True):
        self.model = model
        self.foreign_key_column = foreign_key_column
        self.uselist = uselist # True para uno-a-muchos, False para uno-a-uno
        self.name = None # Se asigna en la metaclass
    """
        args:
            * instance: es la instancia del modelo a la que se accede (ej. mi_producto)
            * owner: es la clase del modelo (ej. Product)
        description: 
            * Este método se llamará automáticamente cada vez que accedas a un atributo de relación, como mi_producto.inventory.    
    """
    def __get__(self, instance, owner):
        # si no hay una instancia, no se puede hacer una consulta:
        if instance is None: 
            return self

        # 1. Obtener el valor de la llave primaria de la instancia actual 
        primary_key_name = instance.primary_key

        # The getattr() function in Python is a built-in function used to retrieve the value of an attribute from an object dynamically. It is particularly useful when the attribute name is not known until runtime. If the specified attribute does not exist, you can provide a default value to avoid an
        primary_key_value = getattr(instance, primary_key_name)

        # 2 asegurarse de que hay una sesion para hacer la consulta 
        if instance._session is None: 
            raise RuntimeError("No db session attached to the model instance")

        # 3 construir la consulta SELECT para el modelo de la relacion.  
        # ejemplo en este caso iria a ProductInventory y buscaria lo que coincida con el id del Product.    
        query_builder = Query(self.model).where(self.foreign_key_column).generate()

        # 4 ejectuar la consulta con la sesion
        # aqui es dodne la magia ocurre, la db sera consultada

        if self.uselist: # para relaciones 1 a muchos
            # consulta para todos los registros relacionados
            result = instance._session.get_all(
                query=query_builder, 
                param=primary_key_value
            )
        else: # para relaciones 1 a 1 

            # consulta para un solo registro relacionado
            result = instance._session.get_one_or_none(
                query=query_builder, 
                param=primary_key_value
            ) 

        # 5. Retornar el resultado de la consulta
        return result



# La meta clase que hara la magia y extraera la info
class MetaSchemaDeclarative(type): 
    """
    __new__ :
    es una función especial que es responsable de crear y devolver la nueva instancia de un objeto.
    """
    def __new__(cls, name, bases, attrs):
        
        # Itera sobre una COPIA de los items para poder modificar el original
        for attr_name, attr_value in attrs.copy().items():
            
            # debe buscar instancias de Relationship en el diccionario attrs, guardar la referencia y,
            #  en el futuro, construir la lógica para realizar la consulta cuando se acceda a ese atributo.
            if isinstance(attr_value, Column) or isinstance(attr_value, ForeignKey):
                attr_value.name = attr_name 
                if attr_value.primary_key:
                    attrs['primary_key'] = attr_name
            
            # AÑADIDO: Si es una relación, le asigna su nombre
            if isinstance(attr_value, Relationship):
                attr_value.name = attr_name
        
            
        # Llama al constructor de clases normal para crear la clase
        return super().__new__(cls, name, bases, attrs)
    
    
# La clase base que utilzia la metaclase   
#  NOTA PARA RECORDAR
"""
El **kwargs en la definición de una función significa que el método puede aceptar un número variable de argumentos de palabra clave (keyword arguments).

Aquí está el desglose de lo que significa y cómo funciona:

** (dos asteriscos): Esto indica que Python debe recoger todos los argumentos que le pasas con un nombre (ej. nombre="Juan", edad=30) y empaquetarlos en un diccionario.

kwargs: Es el nombre de la variable que contendrá ese diccionario. 
Podrías llamarla de otra forma (por ejemplo, **atributos), pero 
**kwargs es una convención estándar en Python que todo el mundo reconoce.

Schema debe tener una forma de acceder a la sesión de la base de datos (gem_session). La forma más sencilla es asignarle una referencia a la sesión a cada instancia del modelo después de que la base de datos la devuelva.

""" 
class Schema(metaclass=MetaSchemaDeclarative):
    
    def __init__(self, **kwargs):
        
        # iterar sobre los argumentos o atributos que se le esten pasando
        for key, value in kwargs.items():

            # asignar cada argumento como un atributo de la isntancia 
            
            setattr(self, key, value)

            self._session = None # se usa para almacenar la sesion


class Mapper(): 
    def init(self, *fields):
        self.join_models = []
        self.fields_for_select = fields
    # def validate_fields(self, model:Schema, fields:list) -> bool:

    #     is_not_a_field = True

    #     for field in fields: 

    #         if not hasattr(model, field.name): 
    #             is_not_a_field = False
                
    #     return is_not_a_field
    
    def validate_fields(self) -> str:

        select_fields = []

        for field in self.fields_for_select: 
            
            for model in self.join_models:

                if hasattr(model, field.name): 
                    select_fields.append(f"{model._tablename_}.{field.name}")

                    if getattr(model, field.name) is not field:
                        raise Exception(f"Field not found on model{model}")
                        
                


        select_clause = ", ".join(select_fields)   

        return select_clause     

    def join(self, models:list[Schema], on_key:str):

        for model in models:

            self.join_models.append(model) 
        
        return self

