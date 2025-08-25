import asyncio
import asyncpg
from asyncpg.pool import Pool
from typing import TypeVar, List, Dict, Any
from pydantic import BaseModel
from pygem.queries_generator import Query

class Field(BaseModel):
    is_primary_key:bool
    name:str
    type:str
    is_null:bool
    name:str


"""
@function: Creates and returns a database connection pool.
@params: 
    - config: A dictionary with the database connection information.
@return: A Pool object.
"""
async def create_db_pool(config) -> Pool:
    """Creates and returns a database connection pool."""
    pool = await asyncpg.create_pool(
        min_size=1,     # Minimum number of open connections
        max_size=10,    # Maximum number of connections
        loop=None,
        **config
    )
    return pool

"""
@function: Deletes all records from a given table.
@params: 
    - table: The name of the table to clean.
    - pool: The database connection pool.
@return: None
"""
async def clean_table(table, pool): 
    async with pool.acquire() as conn:
        await conn.execute(f"DELETE FROM {table}")


"""
@class: Represents the schema of a database table.
@params: 
    - table: The name of the table.
    - primary_key: The name of the primary key.
    - fields: A list of Field objects that describe the table's fields.
@return: An instance of the Schema class.
"""
class Schema:
    """
    @method: Initializes the table schema.
    @params:
        - table: The name of the table.
        - primary_key: The name of the primary key.
        - fields: A list of Field objects that describe the table's fields.
    @return: None
    """
    def __init__(self, table: str, primary_key: str, fields: list):
        self.table = table
        self.primary_key = primary_key
        self.fields = fields

    """
    @method: Gets the name of the table.
    @params: None
    @return: The table name as a string.
    """
    def get_table(self) -> str:
        return self.table

    """
    @method: Gets the name of the primary key.
    @params: None
    @return: The primary key name as a string.
    """
    def get_main_key(self) -> str:
        return self.primary_key

    """
    @method: Gets a list of the names of all table fields.
    @params: None
    @return: A list of strings with the field names.
    """
    def get_all_table_fields(self) -> list[str]:
        return [field.name for field in self.fields]

    """
    @method: Converts a list of fields into a comma-separated string.
    @params: 
        - fields: A list of strings with the field names.
    @return: A string with the fields joined by commas.
    """
    def convert_fields_to_string(self, fields: list[str]) -> str:
        return ', '.join(fields)


    """
    @method: Since we need an alias when we're working with many to many this funciton returns the table alias
    @params: 
        - fields: n/a
    @return: the table alias 
    """
    def get_alias(self) -> str:
        # """
        # Devuelve el alias de la tabla. Si la tabla es 'products_inventory',
        # el alias es 'pi'. Si la tabla es 'users', el alias es 'u'.
        # """
        # table_parts = self.table.split('_')
        
        # if len(table_parts) > 1:
        #     alias = ''.join([part[0] for part in table_parts])
        #     return alias.lower()
        # else:
        #     return self.table[0].lower()
        # por el momento lo pondre a que el alias sea igual al nombre de la tabla
        return self.get_table()
    
    """
    @method: Generates a list of placeholders for an insert query ($1, $2, etc.).
    @params: None
    @return: A list of strings with the placeholders.
    """
    def get_query_params_for_insert(self) -> list[str]:
        return [f"${i + 1}" for i in range(len(self.fields))]

    """
    @method: Generates a list of field assignments for an update query.
    @params: None
    @return: A list of strings in the format 'field = $N'.
    """
    def get_query_params_for_update(self) -> list[str]:
        fields_to_set = []
        param_index = 2
        for field in self.fields:
            if not field.is_primary_key:
                fields_to_set.append(f"{field.name} = ${param_index}")
                param_index += 1
        return fields_to_set

# ---
"""
@class: Generates generic SQL queries for a single table.
@params:
    - schema: An instance of the Schema class.
@return: An instance of the SingleQueries class.
"""
class SingleQueries:
    """
    @method: Initializes the query generator class with a schema.
    @params:
        - schema: An instance of the Schema class.
    @return: None
    """
    def __init__(self, schema: Schema):
        self.schema = schema
        self.query_generator = Query()

    """
    @method: Generates an SQL query to select all records from the table.
    @params: None
    @return: A string with the SQL query.
    """
    # def select_query(self) -> str:
    #     all_fields = self.schema.get_all_table_fields()
    #     all_fields_str = self.schema.convert_fields_to_string(all_fields)
    #     return f"SELECT {all_fields_str} FROM {self.schema.get_table()}"

    def select_query(self) -> str: 

        table = self.schema.get_table()
        table_fields = self.schema.get_all_table_fields()
        table_fields_to_string = self.schema.convert_fields_to_string(table_fields)
        
        
        query = self.query_generator.select_query(
            query_type=type,
            table=table, 
            table_fields_to_string=table_fields_to_string,
            where=None
            )

        return query

    
    """
    @method: Generates an SQL query to select a record by its primary key.
    @params: None
    @return: A string with the SQL query.
    """
    def select_query_with_principal_key(self) -> str:

        table = self.schema.get_table()
        table_fields = self.schema.get_all_table_fields()
        table_fields_to_string = self.schema.convert_fields_to_string(table_fields)
        main_key = self.schema.get_main_key()
        
        query = self.query_generator.select_query(
            query_type=type,
            table=table, 
            table_fields_to_string=table_fields_to_string,
            where=(main_key)
            )

        return query

    
    """
    @method: Generates an SQL query to select a record by a given key.
    @params: 
        - key: The name of the key to filter by.
    @return: A string with the SQL query.
    """
    def select_query_with_key(self, key) -> str:
        # all_fields = self.schema.get_all_table_fields()
        # all_fields_str = self.schema.convert_fields_to_string(all_fields)
        # return f"SELECT {all_fields_str} FROM {self.schema.get_table()} WHERE {key} = $1"
        
        query = self.query_generator.generate(
            gem = self.schema,
            type="SELECT",
            fields="ALL",
            where=key,
            limit=False,
            offset=False
            )

        return query
    
        
    """
    @method: Generates an SQL query to select all records from the table with 
    limits ideal for paginated results.
    @params: None
    @return: A string with the SQL query.
    """
    def select_query_with_limits(self) -> str:
        # all_fields = self.schema.get_all_table_fields()
        # all_fields_str = self.schema.convert_fields_to_string(all_fields)
        # return f"SELECT {all_fields_str} FROM {self.schema.get_table()} ORDER BY {self.schema.get_main_key()} ASC LIMIT $1 OFFSET $2"
    
        query = self.query_generator.generate(
            gem = self.schema,
            type="SELECT",
            fields="ALL",
            where=None,
            limit=True,
            offset=True
            )

        return query
    
    def select_items_by_ids_query(self):
        return f"SELECT * FROM {self.schema.get_table()} WHERE {self.schema.get_main_key()} = ANY($1::uuid[])"
    
    """
    @method: Generates an SQL query to select all records from the table with 
    limits ideal for paginated results.
    @params: None
    @return: A string with the SQL query.
    """
    """
        Tengo una tabla de many to many llamada product_categories 
        donde tengo el id de products y el id de categoria.
        Quiero hacer un select para mandando la categoria
        me devuelva todos los products que la contengan. 
    """
    # def select_query_paginated_with_many_to_many(self, many_to_many_gem:Schema, second_gem:Schema) -> str:

    #     main_gem_table = self.schema.get_table()
    #     main_gem_alias = self.schema.get_alias()
    #     main_gem_mk = self.schema.get_main_key()

    #     second_gem_table = second_gem.get_table()
    #     second_gem_alias = second_gem.get_alias()
    #     second_gem_mk = second_gem.get_main_key()

    #     many_to_many_alias = self.schema.get_alias() + second_gem.get_alias()
    #     many_to_many_table = many_to_many_gem.get_table()

    #     query = f"""SELECT {self.schema.get_alias()}.* FROM {main_gem_table} AS {main_gem_alias} JOIN {many_to_many_table} AS {many_to_many_alias} ON {main_gem_alias}.{main_gem_mk} = {many_to_many_alias}.{main_gem_mk} JOIN {second_gem_table} AS {second_gem_alias} ON {many_to_many_alias}.{second_gem_mk} = {second_gem_alias}.{second_gem_mk} WHERE {second_gem_alias}.{second_gem_mk} = $1 LIMIT $2 OFFSET $3"""
        
    #     """this is the expected output

    #     SELECT
    #         p.*
    #     FROM
    #         products AS p
    #     JOIN
    #         product_categories AS pc ON p.product_id = pc.product_id
    #     JOIN
    #         categories AS c ON pc.category_id = c.category_id
    #     WHERE
    #         c.category_id = $1;
        
    #     """
    #     return query
    
    # key_value is the name of the table field like name, description, etc
    def select_paginated_with_like_query(self, field_name:str):
        if self.validate_fields(field_name):

            return f"""SELECT * FROM {self.schema.get_table()} WHERE {field_name} ILIKE $1 ORDER BY product_id LIMIT $2 OFFSET $3"""
    
    # TODO: 
    # hacer la query mas custom
    def select_by_user_id(self) -> str:

        # all_fields = self.schema.get_all_table_fields()
        # all_fields_str = self.schema.convert_fields_to_string(all_fields)
        # return f"SELECT {all_fields_str} FROM {self.schema.get_table()} WHERE user_id=$1"
    
        query = self.query_generator.generate(
            gem = self.schema,
            type="SELECT",
            fields="ALL",
            where="user_id",
            limit=False,
            offset=False
            )

        return query

    # una query sql para logins. 
    def select_username_login(self):
        key="username"
        return self.select_query_with_key(key)
    
    # TODO
    def select_products_by_its_id_with_stock_query(self): 
        main_table = self.schema.get_table()
        main_key = self.schema.get_main_key()

        query = f"SELECT p.product_id, p.unit_price, pi.stock FROM {main_table} AS p JOIN products_inventory AS pi ON p.{main_key} = pi.product_id WHERE p.{main_key} = ANY($1::uuid[])"

        return query
    
    # TODO
    """
    @method: Generates an SQL query to insert a new record.
    @params: None
    @return: A string with the SQL query.
    """
    def insert_query(self) -> str:
        table_fields = self.schema.get_all_table_fields()
        table_fields_str = self.schema.convert_fields_to_string(table_fields)
        
        query_params = self.schema.get_query_params_for_insert()
        query_params_str = self.schema.convert_fields_to_string(query_params)
        
        return f"INSERT INTO {self.schema.get_table()} ({table_fields_str}) VALUES ({query_params_str}) RETURNING {table_fields_str}"

    # TODO
    """
    @method: Generates an SQL query to update a record.
    @params: None
    @return: A string with the SQL query.
    """
    def update_query(self) -> str:
        all_fields_str = self.schema.convert_fields_to_string(self.schema.get_all_table_fields())
        query_params_for_update = self.schema.get_query_params_for_update()
        query_params_for_update_str = self.schema.convert_fields_to_string(query_params_for_update)
        
        return f"UPDATE {self.schema.get_table()} SET {query_params_for_update_str} WHERE {self.schema.get_main_key()} = $1 RETURNING {all_fields_str}"
    # TODO
    """
    @method: Generates an SQL query to delete a record.
    @params: None
    @return: A string with the SQL query.
    """
    def delete_query(self) -> str:
        all_fields_str = self.schema.convert_fields_to_string(self.schema.get_all_table_fields())
        return f"DELETE FROM {self.schema.get_table()} WHERE {self.schema.get_main_key()} = $1 RETURNING {all_fields_str}"
    # TODO
    def delete_query_customized_field_query(self, field_name:str) -> str:
        if self.validate_fields(field_name):

            return f"DELETE FROM {self.schema.get_table()} WHERE {field_name} = $1 "

    # util para validar que un field name mandado como parametro 
    # realmente pertenece a la lsita de fields validso del schema. 
    # Esto con el fin de evitar la SQL inyection
    # TODO
    def validate_fields(self, field_name:str) -> bool:
        # tomar todos los fields
        all_fields = self.schema.get_all_table_fields()

        if field_name not in all_fields:

            raise Exception("Invalid request 5555")

        return True

# ---
"""
@class: Represents a generic single-table schema.
@params:
    - table: The name of the table.
    - primary_key: The name of the primary key.
    - fields: A list of Field objects that describe the table's fields.
@return: An instance of the SingleGenericSchema class.
"""
class SingleGenericSchema(Schema):
    """
    @method: Initializes the schema and the query generator.
    @params:
        - table: The name of the table.
        - primary_key: The name of the primary key.
        - fields: A list of Field objects that describe the table's fields.
    @return: None
    """
    def __init__(self, table: str, primary_key: str, fields: list):
        super().__init__(table, primary_key, fields)
        self.queries = SingleQueries(self) 

# ---
T = TypeVar('T', bound=BaseModel)

"""
@class: Manages database interaction using asyncpg.
@params:
    - schema_entity: An instance of SingleGenericSchema.
    - pool: The database connection pool.
@return: An instance of the DBManager class.
"""
class DBManager:
    """
    @method: Initializes the database manager.
    @params:
        - schema_entity: An instance of SingleGenericSchema.
        - pool: The database connection pool.
    @return: None
    """
    def __init__(self, schema_entity: SingleGenericSchema, pool: Pool):
        self.schema_entity = schema_entity
        self.pool = pool
        
    """
    @method: Gets all records from the table.
    @params: None
    @return: A list of dictionaries with the database records.
    """
    async def get_all(self) -> List[Dict[str, Any]]:
        query = self.schema_entity.queries.select_query()
        async with self.pool.acquire() as conn:
            records = await conn.fetch(query)
            return [dict(record) for record in records]
    
    async def get_product_by_id(self, product_id:str)-> Dict[str, Any]:
        query = self.schema_entity.queries.select_join_by_main_id()

        async with self.pool.acquire() as conn: 
            records = await conn.fetch(query, product_id)
            if records:
                return dict(records[0])
        
        return None

    """
        Esto deberia devolver la informacion de dos tablas conectadas si pasamos el id del usuario. 
    """ 
    async def get_join_by_user_id(self, user_id:str)-> Dict[str, Any]:
        query = self.schema_entity.queries.select_by_user_id()

        async with self.pool.acquire() as conn:
            records = await conn.fetch(query, user_id)
            return [dict(record) for record in records]
        


    # login
    async def get_by_username(self, username:str)-> Dict[str, Any]:

        query = self.schema_entity.queries.select_username_login()
        async with self.pool.acquire() as conn: 
            records = await conn.fetch(query, username)
            if records:
            # records[0] es el objeto de un solo registro.
            # Puedes convertirlo a un dict.
                return dict(records[0]) 
            
        return None
        
    """
    @method: Gets a single record by its primary key.
    @params: 
        - key_value: The primary key value of the record to find.
    @return: A dictionary with the record or None if not found.
    """
    async def get_by_principal_key(self, key_value) -> Dict[str, Any] | None:
        query = self.schema_entity.queries.select_query_with_principal_key()
        async with self.pool.acquire() as conn:
            record = await conn.fetchrow(query, key_value)
            return dict(record) if record else None
        
    async def get_all_by_key(self, key_name: str, key_value: str) -> list[dict[str, any]] | None:
        
        # 1. Get the list of all valid field names from your schema.
        valid_fields = self.schema_entity.get_all_table_fields()
        
        # 2. Check if the provided key_name exists in the list of valid fields.
        if key_name not in valid_fields:
            # 3. If it does not exist, raise a ValueError with a clear message.
            raise ValueError(f"Invalid field name")

        # 4. If the key_name is valid, proceed with building and executing the query.
        query = self.schema_entity.queries.select_query_with_key(key_name)

        async with self.pool.acquire() as conn:
            records = await conn.fetch(query, key_value)
            return [dict(record) for record in records]
        
    # luego debo de personalizar esto para hacerlo generico. 
    # por el momento solo quiero que me devuelva la info de los productos mas la cantidad actual de esos productos en el carrito 
            #     
    async def get_all_products_on_cart(self) -> List[Dict[str, Any]]:
        query = self.schema_entity.queries.select_query()
        async with self.pool.acquire() as conn:
            records = await conn.fetch(query)
            return [dict(record) for record in records]
        
    """
    @method: Select all the records from the db but using a paginated result
    @params: 
        - limit: 
        - offset:
    @return: A list of items limited to the pagination
    """
    async def get_all_paginated(self, limit:int,offset:int) -> List[Dict[str, Any]] | None:
        
        query = self.schema_entity.queries.select_query_with_limits()
        async with self.pool.acquire() as conn:
            records = await conn.fetch(query, limit, offset)
            return [dict(record) for record in records]

    
    async def get_all_paginated_like(
            self, 
            key_value:str, 
            field_key_name:str, 
            limit:int,
            offset:int
        ):
        
        # 1. Obtenemos la lista de campos válidos de forma dinámica usando tu función.
        #    Esto garantiza que siempre tengamos una lista actualizada y precisa.
        allowed_fields = self.schema_entity.get_all_table_fields()
        # 2. Validamos que el nombre de campo que llega como entrada esté en la lista blanca.
        #    Si no coincide, lanzamos una excepción.
        if field_key_name not in allowed_fields:
            raise ValueError(f"Field name '{field_key_name}' not allowed.")
        
        query = self.schema_entity.queries.select_paginated_with_like_query(field_key_name) 

        # para que funcione correctamente
        pattern_value = f"%{key_value}%"

        async with self.pool.acquire() as conn:
            records = await conn.fetch(query, pattern_value, limit, offset)
            return [dict(record) for record in records]


    """
    @method: Selects records from the main table that are related to a specific item
    in a secondary table, using a many-to-many relationship, with pagination.
    @params: 
        - many_to_many_table: The name of the junction table (e.g., 'product_categories').
        - second_table: The name of the related table to filter by (e.g., 'categories').
        - second_table_main_key: The main key of the second table (e.g., 'category_id').
        - filter_key_value: The specific ID value to filter the results (e.g., '3e9a...').
        - limit: The maximum number of records to return.
        - offset: The number of records to skip from the beginning.
    @return: A list of dictionaries of items, or None if no records are found.
    """

    async def get_all_many_to_many_paginated(self, 
        many_to_many_gem: Schema, 
        second_table_gem: Schema,
        filter_key_value: str,  # Nuevo parámetro para filtrar por el ID
        limit: int, 
        offset: int
    ) -> List[Dict[str, Any]] | None:
        
        query = self.schema_entity.queries.select_query_paginated_with_many_to_many(
            many_to_many_gem=many_to_many_gem, 
            second_gem=second_table_gem
        )
        async with self.pool.acquire() as conn:
            records = await conn.fetch(query, filter_key_value, limit, offset)
            print(records)
            return [dict(record) for record in records]

    # para solucionar el problema 1 + n cuando necesitas datos de varios a la vez
    async def get_items_by_ids_with_transaction(self, items_id: list[str], conn: asyncpg.Connection):

        query = self.schema_entity.queries.select_products_by_its_id_with_stock_query()

        records = await conn.fetch(query, items_id)
        
        # ¡Corregido! Ahora se asegura que los datos sean diccionarios.
        return [dict(record) for record in records]
    

    """
    @method: Creates a new record in the database.
    @params:
        - data: A dictionary with the data for the new record.
    @return: A dictionary with the created record or None if the operation fails.
    """
    async def create(self, data: dict) -> Dict[str, Any] | None:
        insert_query = self.schema_entity.queries.insert_query()
        
        values = [data.get(field.name) for field in self.schema_entity.fields]

        async with self.pool.acquire() as conn:
            record = await conn.fetchrow(insert_query, *values)
            return dict(record) if record else None

    # metodo para crear un nuevo item pero recibiendo una conexion abierta, esto con el fin de ejectuar transacciones SQL 
    async def create_with_transaction(self, data:dict ,conn: asyncpg.Connection) -> Dict[str, Any] | None:

        insert_query = self.schema_entity.queries.insert_query()
        values = [data.get(field.name) for field in self.schema_entity.fields]

        # Usa la conexión pasada como parámetro
        record = await conn.fetchrow(insert_query, *values)
        return dict(record) if record else None

    """
    @method: Updates a record by its primary key.
    @params:
        - key_value: The primary key value of the record to update.
        - data: A dictionary with the data to update.
    @return: A dictionary with the updated record or None if not found.
    """
    async def update(self, key_value, data: dict) -> Dict[str, Any] | None:
        update_query = self.schema_entity.queries.update_query()
        
        update_fields = [field for field in self.schema_entity.fields if not field.is_primary_key]
        update_values = [data.get(field.name) for field in update_fields]
        
        # Fixed: The key_value must come first to match the SQL query's parameter order.
        params = [key_value] + update_values
        
        async with self.pool.acquire() as conn:
            record = await conn.fetchrow(update_query, *params)
            return dict(record) if record else None

    """
    @method: Delete a record by its primary key.
    @params:
        - key_value: The primary key value of the record to delete.
    @return: A dictionary with the deleted record or None if not found.
    """
    async def delete(self, key_value) -> Dict[str, Any] | None:
        delete_query = self.schema_entity.queries.delete_query()
        async with self.pool.acquire() as conn:
            record = await conn.fetchrow(delete_query, key_value)
            return dict(record) if record else None

    # para las transacciones     
    async def delete_by_custom_field_with_transaction(self, field_name:str, key_value:str, conn: asyncpg.Connection) -> bool:

        query = self.schema_entity.queries.delete_query_customized_field_query(field_name)

        record = await conn.execute(query, key_value)

        # If rows_deleted is greater than 0, it means a record was removed.
        if record:
            return True
        else:
            # If no rows were deleted (rows_deleted is 0) or the command failed for some reason.
            return False
        
        
"""
@class: A generic base class for repositories, adaptable to any Pydantic model.
@params:
    - model: The Pydantic model for the repository.
    - gem: The generic table schema.
    - pool: The database connection pool.
@return: An instance of the GemRepository class.
"""
class GemRepository:
    """
    @method: Initializes the repository with the model, schema (gem), and connection pool.
    @params:
        - model: The Pydantic model for the repository.
        - gem: The generic table schema.
        - pool: The database connection pool.
    @return: None
    """
    def __init__(self, model: T, gem: SingleGenericSchema, pool: Pool):
        self.model = model
        self.pool = pool
        self.gem = gem
        self.manager = DBManager(self.gem, self.pool)

    """
    @method: Gets all records and converts them to a list of model objects.
    @params: None
    @return: A list of T model objects.
    """
    async def get_all(self) -> List[T]:
        db_data = await self.manager.get_all()
        return [self.model(**data) for data in db_data]

    # TODO Doc string
    async def get_by_user_id(self, user_id: str) -> T:
        # 1. get_join_by_user_id returns a single record (dict) or None
        # db_data = await self.manager.get_join_by_user_id(user_id)

        db_data = await self.manager.get_join_by_user_id(user_id)
        return [self.model(**data) for data in db_data]
    
    # TODO Doc string
    async def get_all_by_user_id(self, user_id: str) -> List[T]:
        # 1. get_join_by_user_id returns a single record (dict) or None
        # db_data = await self.manager.get_join_by_user_id(user_id)

        db_data = await self.manager.get_join_by_user_id(user_id)
        return [self.model(**data) for data in db_data]

    """
    @method: Gets a record by its primary key and converts it to a model object.
    @params: 
        - key_value: The primary key value.
    @return: A T model object or None if not found.
    """
    async def get_by_id(self, key_value) -> T | None:
        db_data = await self.manager.get_by_principal_key(key_value)
        if db_data:
            return self.model(**db_data)
        return None
    
    # login
    async def get_by_username(self, key_value) -> T | None:
        db_data = await self.manager.get_by_username(key_value)
        if db_data:
            return self.model(**db_data)
        return None
    
    """
    @method: gets all the items but paginated with a limit of items per data.
    @params: 
        - limit: 
        - offset: 
    @return: A T model object or None if not found.
    """
    async def get_all_paginated(self, limit:int, offset:int) -> List[T]:
        
        db_data = await self.manager.get_all_paginated(limit, offset)
        return [self.model(**data) for data in db_data] 
    
    
    """
    @method: Creates a new record and converts it to a model object.
    @params:
        - data: A T model object with the data to create.
    @return: A created T model object or None if the operation fails.
    """
    async def create(self, data: T) -> T | None:
        db_data = await self.manager.create(data.model_dump())
        if db_data:
            return self.model(**db_data)
        return None
    
    # para crear un nuevo objeto pero no es necesario devolver el objeto creado, solo si fue exitioso o no 
    async def create_no_returning(self, data: T) -> bool:

        db_data = await self.manager.create(data.model_dump())

        if db_data:
            return True
        return False


    # TODO: doc strimgs Por el momento es para crear una transaccion.
    async def create_with_transaction(self, data: T, conn: asyncpg.Connection = None) -> T | None:
        # Convert the Pydantic model to a dictionary using .model_dump()
        db_data = await self.manager.create_with_transaction(data, conn)

        if db_data:
            return self.model(**db_data)
        return None

    """
    @method: Updates a record and converts it to a model object.
    @params:
        - key_value: The primary key value of the record to update.
        - data: A T model object with the data to update.
    @return: An updated T model object or None if not found.
    """
    async def update(self, key_value, data: T) -> T | None:
        db_data = await self.manager.update(key_value, data.model_dump())
        if db_data:
            # Fixed: Return the full object so the test can pass.
            return self.model(**db_data)
        return None
        
    """
    @method: Deletes a record and converts it to a model object.
    @params:
        - key_value: The primary key value of the record to delete.
    @return: A deleted T model object or None if not found.
    """
    async def delete(self, key_value) -> T | None:
        db_data = await self.manager.delete(key_value)
        if db_data:
            return self.model(**db_data)
        return None