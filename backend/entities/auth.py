from pydantic import BaseModel

class LoginRequest(BaseModel):

    username:str
    password:str
    is_admin:bool
    
    