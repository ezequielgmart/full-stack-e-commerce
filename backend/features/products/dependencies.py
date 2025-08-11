from fastapi import Depends
from config.connect import DbPool, DB_CONFIG
from pygem.main import create_db_pool
from .repository import ProductRepository
from .service import ProductService
from .controller import ProductController

async def get_db_pool():
    pool = await create_db_pool(DB_CONFIG)
    try: 
        yield pool
    finally:
        pool.close()

async def get_product_repository(pool:DbPool = Depends(get_db_pool)):
    return ProductRepository(pool=pool)

async def get_product_service(repository: ProductRepository = Depends(get_product_repository)):
    return ProductService(repository=repository)

async def get_product_controller(service: ProductService = Depends(get_product_service)):
    return ProductController(service=service)        