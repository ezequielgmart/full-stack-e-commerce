from typing import List, Optional
from entities.auth import LoginRequest
from entities.users import User
from .repository import AuthRepository

class AuthService:
    def __init__(self, repository:AuthRepository):
        self.repository = repository

    async def login(self, username: str) -> Optional[User]:
        return await self.repository.get_by_username(username)

        
