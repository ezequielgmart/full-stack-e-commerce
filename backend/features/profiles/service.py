
from entities.profiles import Profile
from .repository import ProfileRepository

class ProfileService:

    def __init__(self, repository:ProfileRepository):
        self.repository = repository

    async def create_profile(self, data:Profile) -> Profile:
        return await self.repository.create(data)
    
    async def get_profile_by_user_id(self, user_id:str) -> Profile:

        return await self.repository.get_by_id(user_id)