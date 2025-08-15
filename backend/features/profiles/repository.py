from entities.profiles import Profile
from pygem.main import GemRepository
from config.connect import DbPool
from entities.migrations import _profiles_gem

class ProfileRepository(GemRepository):

    def __init__(self, pool:DbPool):
        self.gem = _profiles_gem
        super().__init__(model=Profile, gem=self.gem, pool=pool)