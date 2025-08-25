from typing import Optional
from .repository import AuthRepository

from entities.users import User, UserPublic

class AuthService:
    def __init__(self, repository:AuthRepository):
        self.repository = repository

    async def login(self, username:str) -> Optional[User]:

        return await self.repository.get_by_username(username)
    
    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        return await self.repository.get_by_id(user_id)


    """
        por motivos de seguridad evito mandar el usuario interno (que contiene la contraseña)
        y mando un "usuario publico" que es data no sensible 
    
    """
    async def get_public_user(self, user_id:str) -> UserPublic | None:
            # 1. Obtienes el usuario completo desde el repositorio (con la contraseña)
            user: User | None = await self.repository.get_by_id(user_id)
            
            # 2. Si el usuario no existe, devuelves None
            if not user:
                return None
                
            # 3. Conviertes el modelo User a UserPublic
            #    Pydantic tomará los atributos del objeto 'user' que coinciden 
            #    con los campos de 'UserPublic' e ignorará 'password'.
            return UserPublic.model_validate(user, from_attributes=True)
    
