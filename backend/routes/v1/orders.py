from fastapi import APIRouter, Depends
from entities.users import User 
from entities.orders import OrderItemRegister # Asume que tienes un modelo de usuario
from features.orders.dependencies import get_order_controller
from features.orders.controller import OrderController

# Importa la dependencia de autenticación
from features.auth.dependencies import get_current_user 

router = APIRouter()

""" GET METHODS """
# @router.get(
#     "/",
#     summary="Get all the products on the the shopping cart",
#     description="..."
    
# )
# async def get_cart_items(
#     controller:ShoppingCartController = Depends(get_cart_controller),
#     current_user: User = Depends(get_current_user) # Usa la dependencia de autenticación
#     ):
    
#     user_id = current_user.user_id

#     return await controller.get_all_cart_items(user_id)
""" POST METHODS """
@router.post(
    "/",
    summary="Create a new order",
    description="This method create a new order. This should be use to take the products from the check out, process the order and then remove from the shopping cart the products"
    
)
async def register_new_order(
    order_register:list[OrderItemRegister],
    controller:OrderController = Depends(get_order_controller),
    current_user: User = Depends(get_current_user) # Usa la dependencia de autenticación
    ):
    
    user_id = current_user.user_id

    return await controller.create_order(user_id, order_register)
