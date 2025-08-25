from entities.users import User
from pygem.main import GEM
from pygem.queries import Query
from entities.models import User
# from entities.migrations import _users_gem


class AuthRepository():
    def __init__(self, gem_session):
        self.gem_session = gem_session

    # method
    async def get_by_username(self, username:str): 

        qrystr = Query(
            User,
            User.user_id,
            User.username,
            User.password,
            User.is_admin
        ).where(User.username).generate()    

        result = await self.gem_session.get_one_or_none(
            model_cls = User,
            query=qrystr,
            param=username
        ) 

        return result 
    
    async def get_by_id(self, username:str): 

        qrystr = Query(
            User,
            User.user_id,
            User.username,
            User.password,
            User.is_admin
        ).where(User.user_id).generate()    

        result = await self.gem_session.get_one_or_none(
            model_cls = User,
            query=qrystr,
            param=username
        ) 

        return result 
# class AuthRepository(GemRepository):

#     def __init__(self, pool:DbPool):
#         self.gem = _users_gem
#         super().__init__(model=User, gem=self.gem, pool=pool)