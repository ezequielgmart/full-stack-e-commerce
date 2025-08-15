from entities.shipping_addresses import ShippingAddress
from pygem.main import GemRepository
from config.connect import DbPool
from entities.migrations import _shipping_addresses_gem

class ShippingAddressesRepository(GemRepository):

    def __init__(self, pool:DbPool):
        self.gem = _shipping_addresses_gem
        super().__init__(model=ShippingAddress, gem=self.gem, pool=pool)