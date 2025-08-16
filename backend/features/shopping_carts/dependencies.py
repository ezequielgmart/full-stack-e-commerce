from fastapi import Depends
from config.connect import DbPool, DB_CONFIG, TOKEN_CONFIG
from pygem.main import create_db_pool
from .repository import ShoppingCartRepository
from .service import ShoppingCartService
from .controller import ShoppingCartController

async def get_db_pool():
    pool = await create_db_pool(DB_CONFIG)
    try: 
        yield pool
    finally:
        pool.close()

async def get_cart_repository(pool:DbPool = Depends(get_db_pool)):
    return ShoppingCartRepository(pool=pool)

async def get_cart_service(
        repository: ShoppingCartRepository = Depends(get_cart_repository)
        ):
    return ShoppingCartService(repository=repository)


async def get_cart_controller(service: ShoppingCartService = Depends(get_cart_service)):
    return ShoppingCartController(service=service)        

