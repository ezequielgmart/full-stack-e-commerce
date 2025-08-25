
from entities.users import User, NewUserResponse, RegisterRequest
from config.connect import TOKEN_CONFIG
from .service import UserService
import uuid

# hash the pass
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserController:

    def __init__(self, service:UserService):
        self.service = service

   
    async def register(self, data:RegisterRequest) -> User:
        
        # hay que hashear la contraseña antes de pasar al servicio
        hashed_password = self.get_password_hash(data.password)

        data_for_service = {
            "user_id":str(uuid.uuid4()),
            "email":data.email,
            "username":data.username,   
            "password":str(hashed_password)
        }

        new_user = NewUserResponse(**data_for_service)

        return await self.service.register(new_user)


    # Hashing y verificación de contraseñas
    def get_password_hash(self, password: str):
        return pwd_context.hash(password)


    def generate_user_id(self, username:str) -> uuid.UUID:
        new_uuid = uuid.uuid4(username)
        return new_uuid
    
