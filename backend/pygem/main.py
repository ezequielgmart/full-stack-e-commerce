import asyncpg
from typing import Any
""" Darle un enfoque de ORM a pygem """


# El ORM
# Esta clase es la responsable de consultar la db. 
class GEM():
    def __init__(self, pool):
        self.pool = pool

    @classmethod
    async def start(cls, config:dict[str, any]):
        """
        Método de fábrica asíncrono para crear una instancia de GEM.
        """
        try: 
            pool = await asyncpg.create_pool(**config)
            return cls(pool)
        except Exception as e:
            print(f"error connecting to DB: {e}")
            return None
    
    def get_session(self):
        return self.pool
    
    async def begin_transaction(self, callback):
        """
            run a set of db operations within a same transaction
            the callback is a async function which contains business logic 

        """

        async with self.pool.acquire() as conn: 
            async with conn.transaction():
                # passing thru param the conexion to the business logic function
                result = await callback(conn)
                return result 
            
    async def get_all(self, query:str, conn=None) -> list[dict]:

        result = await self._select(
            query=query,
            params=None,
            conn=conn
        )

        return result
        
        
    async def get_one_or_none(self, query:str, param:str, conn=None) -> dict | None:

        record = await self._select(
            query=query,
            params=param,
            conn=conn
        )

        if record: 
            return dict(record[0])
            
        return None    

    async def create(self, model_object: object, conn=None)-> dict | None:
        
        _manager = Add(obj=model_object)
        
        query = _manager.query()
        values = _manager.get_values()

        return await self._insert(
            query=query, 
            values=values, 
            conn=conn
        )
    
    # 'param' debería ser una lista o tupla
    async def remove(self, query: str, param: list, conn=None) -> bool:
        rows_affected = await self._delete(
            query=query,
            params=param,
            conn=conn
        )
        if rows_affected > 0:
            return True
        else: 
            return False    

    
    async def remove_rows_affected(self, query: str, param: list, conn=None) -> int:

        rows_affected = await self._delete(
            query=query,
            params=param,
            conn=conn
        )

        return rows_affected

    async def _delete(self, query: str, params: list, conn=None):
        if conn is None:
            async with self.pool.acquire() as conn:
                # Pasa la lista de parámetros
                rows_deleted = await self._execute_db(query=query, params=params, conn=conn)
        else:
            rows_deleted = await self._execute_db(query=query, params=params, conn=conn)
        
        return rows_deleted



    async def _select(self, query:str, params:str = None, conn=None)-> dict | None:
        
        # Si no se pasa una conexión, adquiere una del pool.
        if conn is None: 
            async with self.pool.acquire() as conn:
                    
                records = await self._fetch_db(
                    query=query,
                    params=params,
                    conn=conn
                )
        else: 
            
            records = await self._fetch_db(
                    query=query,
                    params=params,
                    conn=conn
                )
    

        return [dict(record) for record in records]
    
    # ambos metodos create y create_with_transaction van a usar esto ya que esta parte es lo mismo.  
    async def _insert(self, query:str, values:list[str, Any], conn=None)-> dict | None:

        if conn is None: 

            async with self.pool.acquire() as conn:
                record = await self._fetch_row_db(
                    query=query, 
                    values=values,
                    conn=conn
                )

        else: 

            record = await self._fetch_row_db(
                query=query, 
                values=values,
                conn=conn
            )
            
        return dict(record) if record else None
    
    # por lo general se usa para los select
    async def _fetch_db(self, query:str, conn, params:list[str]=None):

        # si la busqueda no tiene parametros
        if params is None:

            records = await conn.fetch(query)

        else: 

            # si tiene parametros add them    
            records = await conn.fetch(query, params)   

        return records
        
    # para los insert  
    async def _fetch_row_db(self, query:str, values:list, conn):

        record = await conn.fetchrow(query, *values)

        return record
    

    # Usa *params para desempaquetar la lista de parámetros
    async def _execute_db(self, query:str, params:list, conn):

        status_string = await conn.execute(query, *params)

        rows_affected = int(status_string.split()[-1])
    
        return rows_affected
    
    async def execute(self, query: str, *args, conn=None):
        """
        Ejecuta un comando SQL que no devuelve filas (INSERT, UPDATE, DELETE, TRUNCATE, etc).
        """
        if conn is None:
            async with self.pool.acquire() as conn:
                return await conn.execute(query, *args)
        else:
            return await conn.execute(query, *args)
        
class Update(): 
    def __init__(self, obj):
        
        self.obj = obj    
        self.clauses = []

    def query(self): 

        table_name = self.obj._tablename_

        clauses_str = " ".join(self.clauses)

        return f"UPDATE {table_name} SET"   

    # dependiendo de todos los parametros que envie para actualizar se hara una serie de parametros para una query segura 

    def params_for_query(self, fields_for_update): 

        return [f"{i + 1}" for i in range(len(fields_for_update))]     
class Delete():
    
    def __init__(self, obj):
        
        self.obj = obj
        self.clauses = []

    def query(self): 

        # Obtiene el nombre de la tabla desde la clase del objeto
        table_name = self.obj._tablename_  

        # Une las cláusulas WHERE, etc.
        clauses_str = " ".join(self.clauses)

        return f"DELETE FROM {table_name} {clauses_str}"
         
    def add_clause(self, filter:str): 
        
        filter_str = filter.name

        self.clauses.append(f"WHERE {filter_str} = $1")

        return self    
     
class Add():
    def __init__(self, obj):
        self.obj = obj
        self.fields_on_schema = {}

    def query(self) -> str:

        # Obtiene el nombre de la tabla desde la clase del objeto
        table_name = self.obj._tablename_  

        # Filtra los attrs para obtener solo los campos del modelo
        # Evita los atributos internos del objeto
        self.fields_on_schema = {k: v for k, v in vars(self.obj).items() if not k.startswith('_')}

        # Extraer los nombres de los campos
        fields = [field for field in self.fields_on_schema.keys()]

        # generar un parametro $1 $2 $3 para consultas sql preparadas    
        param_values = [f"${i + 1}" for i in range(len(fields))]

        # unir los nombres de los campos y los paramentros por comas
        fields_str = ", ".join(fields)
        params_str = ", ".join(param_values)

        return f"INSERT INTO {table_name} ({fields_str}) VALUES ({params_str}) RETURNING {fields_str}"

    def get_values(self) -> list[str, Any]: 
        # extraer los valores
        return [value for value in self.fields_on_schema.values()]

# El método para construir las consultas SELECT. Solo es responsable de generar las consultas. 
class Query(): 
    # El método para construir las consultas SELECT
    def __init__(self, model, *fields): # Recibe los campos ya desempaquetados

        self.model = model
        self.clauses = []

        # Si la tupla de campos está vacía, se seleccionarán todos los campos (*)
        if not fields:
            self.fields_to_select = "*"
        else:
            # De lo contrario, se usarán los campos específicos
            self.fields_to_select = fields

    def generate(self) -> str: 
        select_clause = ""

        if self.fields_to_select == "*":
            select_clause = "*"
        else:
            # Si se especificaron campos, extrae sus nombres
            select_fields_str = [field.name for field in self.fields_to_select]
            select_clause = ", ".join(select_fields_str)
        
        # Une las cláusulas WHERE, etc.
        clauses_str = " ".join(self.clauses)

        return f"SELECT {select_clause} FROM {self.model._tablename_} {clauses_str}" 
    
    def add_filter(self, filter:str): 
        
        filter_str =  filter.name

        self.clauses.append(f"WHERE {filter_str} = $1")

        return self
    
# Clase de una columna simple
class Column():
    def __init__(self, type, primary_key = False):
            
        self.type = type
        self.name = None # El nombre es inicialmente None
        self.primary_key = primary_key # El nombre es inicialmente None


# La meta clase que hara la magia y extraera la info
class MetaSchemaDeclarative(type): 
    """
    __new__ :
    es una función especial que es responsable de crear y devolver la nueva instancia de un objeto.
    """
    def __new__(cls, name, bases, attrs):
        # itera sobre los atributos que se van a añadir a la clase
        for attr_name, attr_value in attrs.items():
            # Si el atributo es una instancia de Column 
            # se le asignara el nombre del atributo al nombre del objeto columna 

            if isinstance(attr_value, Column):
                attr_value.name = attr_name 

        # llamar al constructor de classes normal para crear la clase
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

""" 
class Schema(metaclass=MetaSchemaDeclarative):
    
    def __init__(self, **kwargs):
        
        # iterar sobre los argumentos o atributos que se le esten pasando
        for key, value in kwargs.items():

            # asignar cada argumento como un atributo de la isntancia 
            setattr(self, key, value)

