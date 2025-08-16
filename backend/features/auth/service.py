from typing import List, Optional
from entities.users import User
from entities.auth import NewUserResponse # solo tiene nombre y password
from entities.shopping_cart import ShoppingCart
from features.shopping_carts.repository import ShoppingCartRepository
from .repository import AuthRepository
import datetime 
import uuid

from entities.users import User, UserPublic


class AuthService:
    def __init__(self, repository:AuthRepository):
        self.repository = repository


    # ir a la base de datos, buscar el usuario por el 
    # nombre de usuario y transformarlo a un User request, 
    # para asi evitar mandar si es admin o no en el frontend
    async def login(self, username:str) -> Optional[User]:

        return await self.repository.get_by_username(username)
    
    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        return await self.repository.get_by_id(user_id)

    
    """
        esto fue movido a users
    
    """
    # async def register(self, user_data: NewUserResponse) -> Optional[User]:
    #     # return await self.repository.create(user_data)

    #     async with self.repository.pool.acquire() as conn:
             
    #         async with conn.transaction():
                 
    #             # register the user
    #             new_user = await self.repository.create_with_transaction(user_data, conn)

    #             if not new_user: 
    #                 # if something fail trying to insert the user it'll create a automatic rollback 
    #                 raise Exception("Failed to register user")
                
    #             new_cart_model = ShoppingCart(
    #                 cart_id=uuid.uuid4(),
    #                 user_id=new_user.user_id,
    #                 created_at=datetime.datetime.now()
    #             )

    #             cart = await self.cart_repository.create_with_transaction(new_cart_model, conn)
                
    #             if not cart: 
    #                 # if something fail trying to insert the users_cart it'll create a automatic rollback 
    #                 raise Exception("Failed to create user's cart")
                
    #             # if both are successfull return the User
    #             return new_user

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
    
