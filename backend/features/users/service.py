from .repository import UserRepository


class UserService:
    def __init__(self, repository:UserRepository):
        self.repository = repository

    async def register_user_with_cart(self, user:dict): 

        user_created = await self.repository.gem_session.begin_transaction(
            lambda conn: UserRepository(self.repository.gem_session).register_user(
                user=user,
                conn=conn
            )
        )

        return user_created