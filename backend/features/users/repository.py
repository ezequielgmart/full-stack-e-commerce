# from entities.users import User
# from pygem.main import GemRepository
# from config.connect import DbPool
# from entities.migrations import _users_gem

# class UserRepository(GemRepository):

#     def __init__(self, pool:DbPool):
#         self.gem = _users_gem
#         super().__init__(model=User, gem=self.gem, pool=pool)


from entities.users import User
from pygem.main import GEM
from pygem.queries import Query
from entities.models import User, ShoppingCart       
import uuid
import datetime

class UserRepository(): 

    def __init__(self, gem_session):
        self.gem_session = gem_session

    async def register_user(self, user: dict, conn):
        new_user = User(
            user_id=user.user_id,
            username=user.username,
            email=user.email,
            password=user.password,
            is_admin=False
        )

        result = await self.gem_session.create(model_object=new_user, conn=conn)

        if not result:
            raise Exception("Failed to register user")

        new_cart_model = ShoppingCart(
            cart_id=uuid.uuid4(),
            user_id=new_user.user_id,
            created_at=datetime.datetime.now()
        )

        cart_result = await self.gem_session.create(
            model_object=new_cart_model, 
            conn=conn
        )

        if not cart_result:
            raise Exception("Failed to register shopping_cart")

        return result
    
