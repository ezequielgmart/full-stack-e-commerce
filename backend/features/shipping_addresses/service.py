from entities.shipping_addresses import ShippingAddress
from .repository import ShippingAddressesRepository

class ShippingAddressesService: 

    def __init__(self, repository:ShippingAddressesRepository):
        self.repository = repository

    async def register_new_shipping_address(self, data:ShippingAddress) -> ShippingAddress:
        return await self.repository.create(data)
    
    async def get_by_id(self, shipping_address_id:str) -> ShippingAddress:

        return await self.repository.get_by_id(shipping_address_id)
    
    
    async def get_all_by_user_id(self, user_id:str) -> ShippingAddress:

        return await self.repository.get_all_by_user_id(user_id)