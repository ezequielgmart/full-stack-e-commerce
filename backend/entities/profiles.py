from pydantic import BaseModel
import uuid

class Profile(BaseModel):

    user_id:uuid.UUID
    first_name:str
    last_name:str
    gender:str


class ProfileRegister(BaseModel):
    
    first_name:str
    last_name:str
    gender:str