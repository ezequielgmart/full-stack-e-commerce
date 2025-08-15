from fastapi import HTTPException, status
from entities.profiles import Profile, ProfileRegister
from .service import ProfileService

class ProfileController:

    def __init__(self, service:ProfileService):
        self.service = service

    async def get_profile(self, current_user_id:str)-> Profile:
        result = await self.service.get_profile_by_user_id(current_user_id)

        if result is None: 
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return result

    async def create_profile(self, current_user_id:str, data:ProfileRegister) -> Profile:

        try:
            
            data_for_service = {
                "user_id":current_user_id,
                "first_name":data.first_name,
                "last_name":data.last_name,  
                "gender":data.gender
            }

            new_profile = await self.service.create_profile(Profile(**data_for_service))

            return new_profile
        
        except (ValueError, TypeError):
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Token expiration time is not configured correctly."
            )
    
        




