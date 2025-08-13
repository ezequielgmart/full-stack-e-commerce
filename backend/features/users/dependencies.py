from fastapi import Depends
from config.connect import DbPool, DB_CONFIG
from pygem.main import create_db_pool
from .repository import UserRepository
from .service import UserService
from .controller import UserController

async def get_db_pool():
    pool = await create_db_pool(DB_CONFIG)
    try: 
        yield pool
    finally:
        await pool.close()

async def get_user_repository(pool:DbPool = Depends(get_db_pool)):
    return UserRepository(pool=pool)

async def get_user_service(repository: UserRepository = Depends(get_user_repository)):
    return UserService(repository=repository)

async def get_user_controller(service: UserService = Depends(get_user_service)):
    return UserController(service=service)        