from fastapi import APIRouter, Depends, Query
from entities.users import User, UserPublic
from features.users.dependencies import get_user_controller
from features.auth.dependencies import get_current_user
from features.users.controller import UserController


# hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

router = APIRouter()

@router.get(
    "/public",
    response_model=UserPublic,
    summary="Obtiene la informacion publica del perfil",
    description="..."
    
)
async def get_public_(

    
    # 1. Esta dependencia valida el token y obtiene el usuario autenticado
    current_user: User = Depends(get_current_user),

    # 2. Esta dependencia te da acceso al controlador para obtener datos adicionales
    controller:UserController = Depends(get_user_controller)
    ):

    """
    La función recibe el objeto 'current_user' automáticamente.
    Si llegamos a este punto, significa que el token es válido.

    # Usas el 'id' del usuario autenticado que te da la dependencia del token.
    # No necesitas pedir el user_id por la URL.

    En este ejemplo:

        * La ruta no necesita un user_id en la URL porque ya sabe quién es el usuario.

        * current_user: User = Depends(get_current_user): FastAPI ejecuta get_current_user, valida el token y pasa el objeto del usuario a esta variable.

        * controller: UserController = Depends(get_user_controller): FastAPI también te provee una instancia de tu UserController, que ya está lista para usarse.

        * Así, get_current_user actúa como un guardián de la ruta, asegurando que solo los usuarios autenticados pasen. Una vez que el guardián ha dado su visto bueno, el resto de la función se ejecuta con normalidad, usando el controlador para realizar las operaciones necesarias.

    """
    return await controller.get_public_user(current_user.user_id)
    
    # password = '12345679'
    # hashed_password = b'$2b$12$2tQkTL7lYSF36YTFSK.Ile/iVWapnDVx0EgQsuV9NoQVnTf6dkBli'

    # # hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # result = bcrypt.checkpw(password.encode('utf-8'), hashed_password)

    # return result
