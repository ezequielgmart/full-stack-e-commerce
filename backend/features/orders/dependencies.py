from fastapi import Depends
from config.connect import DbPool, DB_CONFIG
from pygem.main import create_db_pool
from .repository import OrderRepository
from .service import OrderService
from .controller import OrderController

async def get_db_pool():
    pool = await create_db_pool(DB_CONFIG)
    try: 
        yield pool
    finally:
        pool.close()

async def get_order_repository(pool:DbPool = Depends(get_db_pool)):
    return OrderRepository(pool=pool)

async def get_order_service(
        repository: OrderRepository = Depends(get_order_repository)
        ):
    return OrderService(repository=repository)


async def get_order_controller(service: OrderService = Depends(get_order_service)):
    return OrderController(service=service)        