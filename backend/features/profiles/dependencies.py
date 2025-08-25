from fastapi import Depends
from config.connect import DbPool, DB_CONFIG
from pygem.main import create_db_pool
from .repository import ProfileRepository
from .service import ProfileService
from .controller import ProfileController

async def get_db_pool():
    pool = await create_db_pool(DB_CONFIG)
    try: 
        yield pool
    finally:
        await pool.close()

async def get_profile_repository(pool:DbPool = Depends(get_db_pool)):
    return ProfileRepository(pool=pool)

async def get_profile_service(repository: ProfileRepository = Depends(get_profile_repository)):
    return ProfileService(repository=repository)

async def get_profile_controller(service: ProfileService = Depends(get_profile_service)):
    return ProfileController(service=service)        