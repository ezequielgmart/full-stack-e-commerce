from fastapi import Depends
from config.connect import DbPool, DB_CONFIG, TOKEN_CONFIG
from pygem.main import create_db_pool
from .repository import UserRepository
from features.shopping_carts.repository import ShoppingCartRepository
from features.shopping_carts.dependencies import get_cart_repository
from .service import UserService
from .controller import UserController
from entities.auth import TokenData # You'll need this Pydantic model for the payload

async def get_db_pool():
    pool = await create_db_pool(DB_CONFIG)
    try: 
        yield pool
    finally:
        pool.close()

async def get_user_repository(pool:DbPool = Depends(get_db_pool)):
    return UserRepository(pool=pool)

async def get_user_service(
        repository: UserRepository = Depends(get_user_repository),
        cart_repo: ShoppingCartRepository = Depends(get_cart_repository)
        ):
    return UserService(repository=repository, cart_repository=cart_repo)

async def get_user_controller(service: UserService = Depends(get_user_service)):
    return UserController(service=service)        
