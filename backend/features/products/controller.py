
from fastapi import HTTPException, status
from typing import List
from entities.product import Product
from .service import ProductService

class ProductController:

    def __init__(self, service:ProductService):
        self.service = service
    
    async def get_all(self, limit:int, offset:int) -> List[Product]:
        return await self.service.get_all_products(limit,offset)
    
    
    async def get_by_id(self, product_id: str) -> Product:
        product = await self.service.get_by_id(product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"id '{product_id}' not found."
            )
        return product
    
    async def get_all_products_by_category(self, filter_key_value:str, limit:int, offset:int) -> List[Product]:

        result = await self.service.get_all_products_by_category(
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
    ) -> List[Product]:

        result = await self.service.get_all_products_by_name_like(
            key_value=key_value,
            limit=limit,
            offset=offset
        )

        return result
         