from fastapi import APIRouter, Depends, Query
from typing import List
from entities.users import User
from entities.auth import LoginRequest

from features.auth.dependencies import get_auth_controller
from features.auth.controller import AuthController


# hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

router = APIRouter()

@router.post(
    "/login",
    response_model=User,
    summary="Obtener todos los products",
    description="Retorna una lista de todos los productos disponibles en el sistema."
    
)
async def login(
    auth_login_request:LoginRequest,
    controller:AuthController = Depends(get_auth_controller)
    ):

    return await controller.login(auth_login_request)
    
    # password = '12345679'
    # hashed_password = b'$2b$12$2tQkTL7lYSF36YTFSK.Ile/iVWapnDVx0EgQsuV9NoQVnTf6dkBli'

    # # hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # result = bcrypt.checkpw(password.encode('utf-8'), hashed_password)

    # return result
