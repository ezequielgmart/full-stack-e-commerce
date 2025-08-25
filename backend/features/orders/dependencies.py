from fastapi import Depends
from config.connect import DbPool, DB_CONFIG
from pygem.main import GEM
from .repository import OrderRepository
from .service import OrderService
from .controller import OrderController

# TODO: adaptar esto al nuevo enfoque de sessiones de GEM
async def get_db_pool():
    gem = await GEM.start(DB_CONFIG)

    try: 
        yield gem
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