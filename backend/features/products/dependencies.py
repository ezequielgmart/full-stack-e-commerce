from fastapi import Depends
from config.connect import DB_CONFIG, TOKEN_CONFIG
from pygem.main import GEM
from .repository import ProductRepository
from .service import ProductService
from .controller import ProductController

async def get_session():
    gem_session = await GEM.start(DB_CONFIG)
    try: 
        yield gem_session
    finally:
        gem_session.pool.close()

async def get_product_repository(gem_session = Depends(get_session)):
    return ProductRepository(gem_session=gem_session)

async def get_product_service(repository: ProductRepository = Depends(get_product_repository)):
    return ProductService(repository=repository)

async def get_product_controller(service: ProductService = Depends(get_product_service)):
    return ProductController(service=service)        