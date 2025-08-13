from typing import List, Optional
from entities.users import User
from .repository import AuthRepository


class AuthService:
    def __init__(self, repository:AuthRepository):
        self.repository = repository

    async def login(self, username: str) -> Optional[User]:
        return await self.repository.get_by_username(username)
    
    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        return await self.repository.get_by_id(user_id)
