import asyncpg
from typing import Any
from pygem.queries import Query, Delete, Update, Add
from pygem.schema import *
""" Darle un enfoque de ORM a pygem """


# El ORM
# Esta clase es la responsable de consultar la db. 
class GEM():
    def __init__(self, pool):
        self.pool = pool

    # Es la unica forma de tener un pool ya que esto es asincrono y los __init__ no pueden serlo. 
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
        
    """ 
    ********************************************
    METODOS EXTERNOS, PARA UTILIZAR EN LOS REPO
    ********************************************
    """   
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
            
         
    async def get_all(self, model_cls: object, query:str, conn=None) -> list[object]:
        
        records = await self._select(
            query=query,
            params=None,
            conn=conn
        )
        
        # Convierte cada registro de diccionario a una instancia del modelo
        model_instances = []
        for record in records:
            instance = model_cls(**record)
            instance._session = self  # Asigna la sesión a la instancia
            model_instances.append(instance)

        return model_instances
        
        
    async def get_one_or_none(
            self, 
            model_cls: object, 
            query:str, 
            param:str, 
            conn=None
        ) -> object | None:

        record = await self._select(
            query=query,
            params=param,
            conn=conn
        )
        
        if record:
            # 1. Crea una instancia del modelo con los datos del registro.
            model_instance = model_cls(**dict(record[0]))
            
            # 2. Asigna la sesión (self) a la nueva instancia
            model_instance._session = self
            
            # 3. Retorna la instancia, lista para navegar por las relaciones
            return model_instance
            
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
    
    # OJO
    # Los valores en values deben de ir enviados en el mismo orden en el cual se esta trabajando. 
    # Ejemplo si en mi query tengo 
    # model.email
    # model.password
    # model.gender

    # debo de enviar los valores en ese mismo orden
    # example.com (nuevo)
    # askdaskdkalsfjakslf (nuevo)
    # female (nuevo)

    async def modify(self, query:str, values:list, conn=None): # aun no se que retorna: 
        # IDEAL: debe de retornar si fue efectivo o no, o el modelo completo pero para eso deberia
        # de traer todo el modelo y no me interesa hacer eso por el id. ya veremos. 

        """update_values = """
        if conn is None:
            async with self.pool.acquire() as conn:
                # Pasa la lista de parámetros
                rows_modified = await self._execute_db(query=query, params=values, conn=conn)
        else:
            rows_modified = await self._execute_db(query=query, params=values, conn=conn)
        
        if rows_modified > 0:
            return True
        else: 
            return False    


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

    """ METODOS INTERNOS """
    async def _delete(self, query: str, params: list, conn=None):
        if conn is None:
            async with self.pool.acquire() as conn:
                # Pasa la lista de parámetros
                rows_deleted = await self._execute_db(query=query, params=params, conn=conn)
        else:
            rows_deleted = await self._execute_db(query=query, params=params, conn=conn)
        
        return rows_deleted



    async def _select(self, query:str, params:str = None, conn=None)-> list[dict]:
        
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
        
        # Asegúrate de retornar una lista de diccionarios, no solo un diccionario
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
    
    # Ideal para ejecutar una query sin esperar nada mas que las rows affected
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
        

    
