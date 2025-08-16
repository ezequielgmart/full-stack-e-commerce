import uuid
from pydantic import BaseModel, EmailStr

class User(BaseModel):

    user_id:uuid.UUID
    username:str
    email:str
    password:str
    is_admin:bool

# this is the public user without the password 
# Here's the information that could be show on the frontend
class UserPublic(BaseModel):

    user_id:uuid.UUID
    username:str
    email:str
    is_admin:bool

# ****************** RESPONSES FROM SERVER
# with the password hashed, the user_id added, and the is_admin field set to false
class NewUserResponse(BaseModel):
    user_id:str
    username:str
    password:str
    email:EmailStr
    is_admin: bool = False

class RegisterRequest(BaseModel):
    username:str
    password:str
    email:EmailStr
