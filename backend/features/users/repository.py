from entities.users import User, UserPublic
from pygem.main import GemRepository
from config.connect import DbPool
from entities.migrations import _users_gem

class UserRepository(GemRepository):

    def __init__(self, pool:DbPool):
        self.gem = _users_gem
        super().__init__(model=User, gem=self.gem, pool=pool)