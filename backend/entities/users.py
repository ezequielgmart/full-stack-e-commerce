import uuid
from pydantic import BaseModel

class User(BaseModel):

    user_id:uuid.UUID
    username:str
    email:str
    password:str
    is_admin:bool
