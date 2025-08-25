import asyncpg
from asyncpg.pool import Pool
from pathlib import Path
from pygem.pydantic_models import Field # Asegúrate de que este módulo esté disponible
from pygem.main import SingleGenericSchema # Esta importación es un supuesto, ajusta según tu estructura
from asyncpg.exceptions import PostgresError

"""
@function: Gets a list of all table names from the 'public' schema.
@params: 
    - pool: An asyncpg connection pool.
@return: A list of strings with table names.
"""
async def get_all_tables(pool: Pool) -> list[str]:
    try:
        async with pool.acquire() as conn: 
            query_tables = """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public' AND table_type = 'BASE TABLE';
            """
            result = await conn.fetch(query_tables)
            tables = [record['table_name'] for record in result]
            return tables
    except asyncpg.exceptions.PostgresError as e:
        print(f"Error al obtener tablas: {e}")
        return []

"""
@function: Gets a table's column information and converts it into a structured dictionary.
@params: 
    - table: The name of the table.
    - pool: An asyncpg connection pool.
@return: A dictionary containing the table's name, primary key, and a list of Field objects.
"""
async def get_fields(table: str, pool: Pool) -> dict:
    primary_key_name = ''
    query = """
        SELECT
            c.column_name, c.data_type, c.is_nullable, c.column_default,
            CASE WHEN tc.constraint_type = 'PRIMARY KEY' THEN 'YES' ELSE 'NO' END AS is_primary_key
        FROM
            information_schema.columns AS c
        LEFT JOIN
            information_schema.constraint_column_usage AS ccu ON c.column_name = ccu.column_name
        LEFT JOIN
            information_schema.table_constraints AS tc ON ccu.constraint_name = tc.constraint_name
        WHERE
            c.table_name = $1 AND c.table_schema = 'public'
        ORDER BY
            c.ordinal_position;
    """
    async with pool.acquire() as conn:
        columns = await conn.fetch(query, table)
        fields = []
        
        primary_key_name = None
        
        for record in columns:
            is_null = record['is_nullable'] != "NO"
            is_primary_key = record['is_primary_key'] == "YES"
            
            # Check and store the primary key name
            if is_primary_key:
                if primary_key_name is None:
                    primary_key_name = record['column_name']
                
            # Standardize the data type
            data_type = record['data_type']
            if data_type == 'character varying':
                data_type = 'varchar'
            
            field = {
                "is_primary_key": is_primary_key,
                "name": record['column_name'],
                "type": data_type,
                "is_null": is_null
            }
            
            # Add the field to the list if it's not already there
            if not any(f.name == field["name"] for f in fields):
                fields.append(Field(**field))

    result = {"table_name": table, "pk": primary_key_name, "fields": fields}
    return result

def migration_file_content(table: str, primary_key_name: str, fields: list) -> str:
    fields_string_list = [
        f"        Field(is_primary_key={field.is_primary_key}, name='{field.name}', type='{field.type}', is_null={field.is_null})"
        for field in fields
    ]
    formatted_fields = ",\n".join(fields_string_list)
    
    return f"""
_{table}_gem = SingleGenericSchema(
    table='{table}',
    primary_key='{primary_key_name}',
    fields=[
{formatted_fields}
    ]
)

"""

def create_all_migrations_file(all_tables_info: list) -> bool:
    try:
        path = Path("./entities/migrations.py")
        full_content = ""
        header = f"""from pygem.main import SingleGenericSchema
from pygem.pydantic_models import Field\n\n"""
        full_content = header
        
        for table_info in all_tables_info:
            content = migration_file_content(
                table_info["table_name"], 
                table_info["pk"], 
                table_info["fields"]
            )
            full_content += content
            
        with open(path, "w") as file:
            file.write(full_content)
        
        return True
    except Exception as e:
        print(f"An error occurred while creating the migrations file: {e}")
        return False

async def main(pool: Pool):
    if pool:
        try:
            db_tables = await get_all_tables(pool)
            
            all_tables_info = []
            if isinstance(db_tables, list):
                for table in db_tables:
                    table_info = await get_fields(table, pool)
                    all_tables_info.append(table_info)

                create_all_migrations_file(all_tables_info)
            else:
                print(db_tables)
        except asyncpg.exceptions.PostgresError as e:
            print(f"Error en la base de datos: {e}")
        finally:
            await pool.close()
    else:
        print("No se pudo crear el pool de la base de datos. Verifica tu archivo .env")

