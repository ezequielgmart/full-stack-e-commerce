from fastapi import HTTPException, status
from typing import List
from entities.users import User, UserPublic
from .service import UserService

class UserController:

    def __init__(self, service:UserService):
        self.service = service

    async def get_public_user(self, user_id:str) -> UserPublic:
        # aqui deberia de estar la verificacion del token.
        #  
        user = await self.service.get_public_user(user_id)  

        if not user:
            # Raise an HTTPException with a 404 status code
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User not found"
            )
        
        return user   
    

