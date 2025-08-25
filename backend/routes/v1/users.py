from fastapi import APIRouter, Depends
from entities.users import RegisterRequest
from features.users.dependencies import get_user_controller
from features.users.controller import UserController

router = APIRouter()


@router.post(
    "/register",
    summary="...",
    description="..."
    
)
async def register(
    new_user:RegisterRequest,
    controller:UserController = Depends(get_user_controller)
    ):

    return await controller.register(new_user)
