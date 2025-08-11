from typing import List, Optional
from entities.product import Product,ProductRequest
from .repository import ProductRepository

class ProductService:
    def __init__(self, repository:ProductRepository):
        self.repository = repository
    
    async def get_by_id(self, product_id: str) -> Optional[Product]:
        return await self.repository.get_by_id(product_id)
    
    
    async def get_all_products(self, limit:int, offset:int) -> List[Product]:
        return await self.repository.get_all_paginated(limit, offset)
    
    async def get_all_products_by_category(self, filter_key_value:str, limit:int, offset:int) -> List[Product]:

        result = await self.repository.get_all_products_by_category(
            filter_key_value=filter_key_value,
            limit=limit,
            offset=offset
        )

        return result
    
    async def get_all_products_by_name_like(
        self,
        key_value:str,
        limit:int,
        offset:int

    ):
        result = await self.repository.get_products_by_name_like(
            key_value=key_value,
            limit=limit,
            offset=offset
        )

        return result


