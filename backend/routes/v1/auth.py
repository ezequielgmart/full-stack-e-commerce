from fastapi import APIRouter, Depends

from entities.auth import LoginRequest, TokenData, TokenResponse
from fastapi.security import OAuth2PasswordBearer
from features.auth.dependencies import get_auth_controller
from features.auth.controller import AuthController


# hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

"""
OAuth2PasswordBearer es una clase de FastAPI que te ayuda a implementar el esquema de seguridad de OAuth2. No implementa OAuth2 completo, sino la parte que es relevante para la autenticación basada en tokens, que es lo que necesitas para tu proyecto.

Su propósito principal es decirle a FastAPI:

Cómo esperar el token: Le indica a FastAPI que el cliente enviará el token en el header Authorization de la solicitud, con el prefijo Bearer. Por ejemplo, Authorization: Bearer mi_token_jwt_aqui.

Dónde obtener el token: Le dice a FastAPI dónde se encuentra el endpoint para obtener el token. Esto es lo que hace el parámetro tokenUrl="token".

El valor que le das a tokenUrl (en este caso, "token") no es el endpoint donde estás ahora (/login). Es el URL que los clientes deben usar para enviar sus credenciales (email y contraseña) y, a cambio, recibir un token.

En tu código, esto se traduce en lo siguiente:

Tu endpoint de login se llama /login.

El esquema de seguridad que define OAuth2PasswordBearer le dice a la documentación de Swagger (la interfaz interactiva de FastAPI) que hay un endpoint llamado /token donde se puede solicitar un token. FastAPI utiliza esta información para configurar la interfaz de usuario de autenticación.
"""
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post(
    "/login",
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
