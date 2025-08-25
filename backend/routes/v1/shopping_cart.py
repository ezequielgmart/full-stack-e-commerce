from fastapi import APIRouter, Depends
from entities.users import User 
from entities.shopping_cart import InsertProduct # Asume que tienes un modelo de usuario
from features.shopping_carts.dependencies import get_cart_controller
from features.shopping_carts.controller import ShoppingCartController

# Importa la dependencia de autenticación
from features.auth.dependencies import get_current_user 

router = APIRouter()

@router.post(
    "/insert/",
    summary="Insert a new product on the shopping cart",
    description="..."
    
)
async def insert_product(
    product:InsertProduct,
    controller:ShoppingCartController = Depends(get_cart_controller),
    current_user: User = Depends(get_current_user) # Usa la dependencia de autenticación
    ):
    
    user_id = current_user.user_id

    return await controller.insert_product_on_cart(user_id, product)

@router.get(
    "/",
    summary="Get all the products on the the shopping cart",
    description="..."
    
)
async def get_cart_items(
    controller:ShoppingCartController = Depends(get_cart_controller),
    current_user: User = Depends(get_current_user) # Usa la dependencia de autenticación
    ):
    
    user_id = current_user.user_id

    return await controller.get_all_cart_items(user_id)

