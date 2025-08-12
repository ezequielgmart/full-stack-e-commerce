from fastapi import Depends
from config.connect import DbPool, DB_CONFIG
from pygem.main import create_db_pool
from .repository import AuthRepository
from .service import AuthService
from .controller import AuthController

async def get_db_pool():
    pool = await create_db_pool(DB_CONFIG)
    try: 
        yield pool
    finally:
        pool.close()

async def get_auth_repository(pool:DbPool = Depends(get_db_pool)):
    return AuthRepository(pool=pool)

async def get_auth_service(repository: AuthRepository = Depends(get_auth_repository)):
    return AuthService(repository=repository)

async def get_auth_controller(service: AuthService = Depends(get_auth_service)):
    return AuthController(service=service)        