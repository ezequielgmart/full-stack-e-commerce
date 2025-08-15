from fastapi import HTTPException, status
from entities.shipping_addresses import ShippingAddress, ShippingAddressRegister
from .service import ShippingAddressesService
import uuid

class ShippingAddressesController:

    def __init__(self, service:ShippingAddressesService):
        self.service = service

    
    async def get_by_id(self, shipping_address_id:str) -> ShippingAddress:

        return await self.service.get_by_id(shipping_address_id)    
    
    # esto debe retornar una lista de todas las direcciones que tiene el usuario que esta
    # actualmente logueado
    async def get_all_by_user_id(self, current_user_id:str) -> list[ShippingAddress]:

        return await self.service.get_all_by_user_id(current_user_id)    

    async def register_new_shipping_address(self, current_user_id:str, data:ShippingAddressRegister) -> ShippingAddress:
      
        data_for_service = {
            
            "address_id":uuid.uuid4(),
            "user_id": current_user_id,
            "recipient_name":data.recipient_name,
            "street_address":data.street_address,
            "city":data.city,
            "state_province":data.state_province,
            "country":data.country,
            "phone_number":data.phone_number,
            "postal_code":data.postal_code,
            "is_default":data.is_default

        }
        
        new_data = await self.service.register_new_shipping_address(ShippingAddress(**data_for_service))

        return new_data

