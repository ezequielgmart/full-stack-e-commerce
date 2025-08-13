import uuid
from pydantic import BaseModel

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

