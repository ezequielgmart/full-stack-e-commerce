from typing import Optional
from entities.orders import OrderItemRegister

from .repository import OrderRepository

class OrderService:

    def __init__(self, repository:OrderRepository):
        self.repository = repository

    async def create_order(self, user_id:str, order_data:list[OrderItemRegister]) -> str:

        return await self.repository.create_order(user_id, order_data)     