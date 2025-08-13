from pydantic import BaseModel
from typing import Optional

class LoginRequest(BaseModel):

    username:str
    password:str
    is_admin:bool
    
# Modelo para la respuesta que contendrá el token
class TokenResponse(BaseModel):

    access_token: str
    token_type: str = "bearer"

    # TODO: 
    # tiempo de expiracion
    # expires_in: Optional[int] = None

# Modelo que define la estructura del token (payload)
class TokenData(BaseModel):

    user_id: Optional[str] = None