from fastapi import APIRouter, Depends
from entities.users import User 
from entities.shipping_addresses import ShippingAddress, ShippingAddressRegister # Asume que tienes un modelo de usuario
from features.shipping_addresses.dependencies import get_shipping_address_controller
from features.shipping_addresses.controller import ShippingAddressesController

# Importa la dependencia de autenticación
from features.auth.dependencies import get_current_user 

router = APIRouter()

@router.post(
    "/",
    summary="...",
    description="..."
)
async def create(
    new_item: ShippingAddressRegister,
    controller: ShippingAddressesController = Depends(get_shipping_address_controller),
    current_user: User = Depends(get_current_user) # Usa la dependencia de autenticación
):
    # En este punto, 'current_user' contiene el objeto del usuario autenticado
    # Puedes usar su ID para asociar el perfil a ese usuario
    user_id = current_user.user_id
    
    # Llama al controlador para crear el perfil
    return await controller.register_new_shipping_address(user_id, new_item)

@router.get(
    "/",
    summary="return all the shipping addresses linked to the current user",
    description="...",
    response_model = list[ShippingAddress]
)
async def get_all(
    controller: ShippingAddressesController = Depends(get_shipping_address_controller),
    current_user: User = Depends(get_current_user) # Usa la dependencia de autenticación
):
    # En este punto, 'current_user' contiene el objeto del usuario autenticado
    # Puedes usar su ID para asociar el perfil a ese usuario
    user_id = current_user.user_id
    
    return await controller.get_all_by_user_id(user_id)

@router.get(
    "/{shipping_address_id}",
    summary="return all the shipping addresses linked to the current user",
    description="...",
    response_model = ShippingAddress
)
async def get_by_id(
    shipping_address_id:str,
    controller: ShippingAddressesController = Depends(get_shipping_address_controller),
    current_user: User = Depends(get_current_user) # Usa la dependencia de autenticación
):
    
    # Llama al controlador pararecibir el perfil del usuario logueado
    return await controller.get_by_id(shipping_address_id)