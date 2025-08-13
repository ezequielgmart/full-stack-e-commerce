from pydantic import BaseModel, EmailStr
from typing import Optional

# ************** REQUESTS****************
# Comming from the register information (the form)
class RegisterRequest(BaseModel):
    username:str
    password:str
    email:EmailStr

class LoginRequest(BaseModel):

    username:str
    password:str
    is_admin:bool


# Modelo que define la estructura del token (payload)
class TokenData(BaseModel):

    user_id: Optional[str] = None

# ****************** RESPONSES FROM SERVER
# with the password hashed, the user_id added, and the is_admin field set to false
class NewUserResponse(BaseModel):
    user_id:str
    username:str
    password:str
    email:EmailStr
    is_admin: bool = False


# Modelo para la respuesta que contendrá el token
class TokenResponse(BaseModel):

    access_token: str
    token_type: str = "bearer"

    # TODO: 
    # tiempo de expiracion
    # expires_in: Optional[int] = None

