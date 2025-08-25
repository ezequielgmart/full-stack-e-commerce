from typing import Any

class Update(): 
    def __init__(self, obj:object, *fields:list):
        
        self.obj:object = obj   
        self.fields_to_update:list = fields
        self.clauses:list = []

    def query(self): 

        table_name = self.obj._tablename_

        clauses_str = " ".join(self.clauses)
        
        fields_to_update_str = [f"{field.name} = ${index + 1}" for index, field in enumerate(self.fields_to_update, start=1)]

        set_fields = ", ".join(fields_to_update_str)

        return f"UPDATE {table_name} SET {set_fields} {clauses_str}"   
    
    def where(self, filter:str): 
        
        if isinstance(filter, str):
            filter_str = filter
        else:
            filter_str = filter.name
        
        self.clauses.append(f"WHERE {filter_str} = $1")

        return self   


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
         
    def where(self, filter:str): 
        
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

class Query():
    def __init__(self, model, *fields):
        self.model = model
        self.clauses = []

        self.fields_to_select = fields if fields else "*"
        self.func_fields = []
        self.where_added: bool = False

        self.join_models = []
        self.joins = []

    def generate(self) -> str:
        select_fields = []
        if self.fields_to_select == "*":
            select_fields.append(f"{self.model._tablename_}.*")
        else:
            all_models = [self.model] + self.join_models
            
            for field in self.fields_to_select:
                found = False
                for model in all_models:
                    if hasattr(model, field.name):
                        select_fields.append(f"{model._tablename_}.{field.name}")
                        found = True
                        break
                
                if not found:
                    raise Exception(f"Field '{field.name}' not found on any of the specified models.")
        
        # La parte que maneja la duplicación
        if len(self.func_fields) > 0:
            group_by_fields = ", ".join(select_fields)
            self.clauses.append(f"GROUP BY {group_by_fields}")
            
            for fun_field in self.func_fields:
                select_fields.append(fun_field)
        
        select_clause = ", ".join(select_fields)
        
        main_table_alias = f"AS {self.get_table_alias(self.model)}"
        
        join_clauses = " ".join([
            f"JOIN {join['join_table']} AS {join['join_alias']} ON {join['on_condition']}"
            for join in self.joins
        ])
        
        clauses_str = " ".join(self.clauses)
        
        return f"SELECT {select_clause} FROM {self.model._tablename_} {main_table_alias} {join_clauses} {clauses_str}".strip()


    def get_table_alias(self, model):
        # Using the full table name as the alias for clarity
        return model._tablename_

    def where(self, filter: str):
        main_table_alias = self.model._tablename_
        self.where_added = True 
        filter_str = filter.name
        # si hay uniones
        if len(self.joins) > 0:

            self.clauses.append(f"WHERE {main_table_alias}.{filter_str} = $1")

        else:

            self.clauses.append(f"WHERE {filter_str} = $1")

        return self

    def array_agg(self, model, field, label:str):

        alias = model._tablename_
        
        self.func_fields.append(f"array_agg({alias}.{field.name}) AS {label}")

        return self 

    def join(self, joined_model, main_on_key, joined_on_key, main_model=None):
        join_alias = self.get_table_alias(joined_model)

        if main_model is None:
            main_alias = self.get_table_alias(self.model)
        else:
            main_alias = self.get_table_alias(main_model)
        
        # Asume que los parámetros son objetos de columna
        main_on_key_name = main_on_key.name
        joined_on_key_name = joined_on_key.name

        on_condition = f"{main_alias}.{main_on_key_name} = {join_alias}.{joined_on_key_name}"

        self.joins.append({
            "join_table": joined_model._tablename_,
            "join_alias": join_alias,
            "on_condition": on_condition
        })
        
        self.join_models.append(joined_model)
        return self

    def paginated(self):

        if self.where_added:
        
            self.clauses.append(f"LIMIT $2 OFFSET $3")
        
        else: 
            
            self.clauses.append(f"LIMIT $1 OFFSET $2")

        return self    
    
    def order_by(self, filter:str):
        
        self.clauses.append(f"ORDER BY {filter.name}")

        return self    
    
    def ilike(self, filter:str):

        self.clauses.append(f"WHERE {filter} ILIKE $1")

    def like(self, filter:str):

        self.clauses.append(f"WHERE {filter} LIKE $1")

    def _function_group_by(self, select_fields):

        selec_fields_clause = ", ".join(select_fields)

        self.clauses.append(f"GROUP BY {selec_fields_clause}")


