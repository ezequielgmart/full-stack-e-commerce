from fastapi import Depends
from config.connect import DbPool, DB_CONFIG
from pygem.main import create_db_pool
from .repository import ShippingAddressesRepository
from .service import ShippingAddressesService
from .controller import ShippingAddressesController

async def get_db_pool():
    pool = await create_db_pool(DB_CONFIG)
    try: 
        yield pool
    finally:
        await pool.close()

async def get_shipping_address_repository(pool:DbPool = Depends(get_db_pool)):
    return ShippingAddressesRepository(pool=pool)

async def get_shipping_address_service(repository: ShippingAddressesRepository = Depends(get_shipping_address_repository)):
    return ShippingAddressesService(repository=repository)

async def get_shipping_address_controller(service: ShippingAddressesService = Depends(get_shipping_address_service)):
    return ShippingAddressesController(service=service)        