from typing import List, Optional
from .repository import ProductRepository

class ProductService:
    def __init__(self, repository:ProductRepository):
        self.repository = repository
    
    # sort_by: filter name like name
    # order: asc or desc
    async def get_all_products(self, limit:int, offset:int, sort_by:str, order:str) -> Optional [list[dict]]:

        return await self.repository.get_all_products(limit=limit, offset=offset, sort_by=sort_by, order=order)
    
    async def get_by_id(self, product_id: str) -> Optional[dict]:
        return await self.repository.get_by_id(product_id)
    
    async def get_all_products_by_category(self, filter_key_value:str, limit:int, offset:int) -> List[dict]:

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
        result = await self.repository.get_all_products_by_name_like(
            value=key_value,
            limit=limit,
            offset=offset
        )

        return result

    async def get_product_by_id_all_details(self, product_id:str)->dict:

        result = await self.repository.get_by_id(product_id)

        return result

