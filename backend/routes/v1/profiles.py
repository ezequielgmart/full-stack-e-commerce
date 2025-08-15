from fastapi import APIRouter, Depends, Query
from entities.profiles import Profile, ProfileRegister
from entities.users import User # Asume que tienes un modelo de usuario
from features.profiles.dependencies import get_profile_controller
from features.auth.dependencies import get_current_user # Importa la dependencia de autenticación
from features.profiles.controller import ProfileController

router = APIRouter()

@router.post(
    "/",
    summary="...",
    description="..."
)
async def create(
    profile: ProfileRegister,
    profile_controller: ProfileController = Depends(get_profile_controller),
    current_user: User = Depends(get_current_user) # Usa la dependencia de autenticación
):
    # En este punto, 'current_user' contiene el objeto del usuario autenticado
    # Puedes usar su ID para asociar el perfil a ese usuario
    user_id = current_user.user_id
    
    # Llama al controlador para crear el perfil
    return await profile_controller.create_profile(user_id, profile)

@router.get(
    "/",
    summary="...",
    description="..."
)
async def create(
    response_model = Profile,
    profile_controller: ProfileController = Depends(get_profile_controller),
    current_user: User = Depends(get_current_user) # Usa la dependencia de autenticación
):
    # En este punto, 'current_user' contiene el objeto del usuario autenticado
    # Puedes usar su ID para asociar el perfil a ese usuario
    user_id = current_user.user_id
    
    # Llama al controlador pararecibir el perfil del usuario logueado
    return await profile_controller.get_profile(user_id)