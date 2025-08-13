import os
import asyncpg
import asyncio
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Define el tipo DbPool para la inyección de dependencias.
DbPool = asyncpg.Pool

# Configuración de la base de datos
DB_CONFIG = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT'))
}

# TODO: arreglar esto del config.
# TOKEN_CONFIG = {
#     'secret_JWT_KEY': os.getenv('SECRET_JWT_KEY'),
#     'algorithm': os.getenv('ALGORITHM '),
#     'access_token_expire_minutes': int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES '))
# }

TOKEN_CONFIG = {
    'secret_JWT_KEY': "Gavilan o paloma",
    'algorithm': "HS256",
    'access_token_expire_minutes': 30
}


async def create_db_pool() -> asyncpg.Pool:
    """
    Crea y retorna un pool de conexiones a la base de datos.
    """
    try:
        pool = await asyncpg.create_pool(**DB_CONFIG)
        return pool
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# # Creamos el pool de conexiones al iniciar la aplicación.
# # Se utiliza asyncio.run() para ejecutar la función asíncrona y obtener el resultado.
# pool = asyncio.run(create_db_pool())