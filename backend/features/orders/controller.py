from fastapi import HTTPException, status
from typing import Optional
from entities.orders import OrderItemRegister
from .service import OrderService

class OrderController:

    def __init__(self, service:OrderService):
        self.service = service

    async def create_order(self, user_id:str, order_data:list[OrderItemRegister]):
        
        return await self.service.create_order(user_id, order_data)
