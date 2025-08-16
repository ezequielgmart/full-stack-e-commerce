from typing import Optional
from entities.users import User, NewUserResponse
from entities.shopping_cart import ShoppingCart

from features.shopping_carts.repository import ShoppingCartRepository
from .repository import UserRepository

import datetime 
import uuid

class UserService:
    def __init__(self, repository:UserRepository, cart_repository:ShoppingCartRepository):
        self.repository = repository
        self.cart_repository = cart_repository
    # ir a la base de datos, buscar el usuario por el 
    # nombre de usuario y transformarlo a un User request, 
    # para asi evitar mandar si es admin o no en el frontend
    
    async def register(self, user_data: NewUserResponse) -> Optional[User]:
        # return await self.repository.create(user_data)

        async with self.repository.pool.acquire() as conn:
             
            async with conn.transaction():
                 
                # register the user
                new_user = await self.repository.create_with_transaction(user_data, conn)

                if not new_user: 
                    # if something fail trying to insert the user it'll create a automatic rollback 
                    raise Exception("Failed to register user")
                
                new_cart_model = ShoppingCart(
                    cart_id=uuid.uuid4(),
                    user_id=new_user.user_id,
                    created_at=datetime.datetime.now()
                )

                cart = await self.cart_repository.create_with_transaction(new_cart_model, conn)
                
                if not cart: 
                    # if something fail trying to insert the users_cart it'll create a automatic rollback 
                    raise Exception("Failed to create user's cart")
                
                # if both are successfull return the User
                return new_user