from entities.product import Product
from pygem.main import GemRepository
from config.connect import DbPool 
from entities.migrations import _products_gem, _categories_gem, _product_categories_gem

class ProductRepository(GemRepository):

    def __init__(self, pool: DbPool):
        self.gem = _products_gem
        super().__init__(model=Product, gem=self.gem, pool=pool)
    """
        @method: Retrieves a paginated list of products belonging to a specific category.
        
        This method uses a many-to-many relationship to find all products
        linked to a given category ID, applying pagination to the results.
        
        @params:
            - filter_key_value (str): The UUID of the category to filter by.
            - limit (int): The maximum number of products to return in the current page.
            - offset (int): The number of products to skip from the beginning of the result set.
            
        @return:
            - List[Dict[str, Any]] | None: A list of dictionaries representing the products,
              or None if no products are found for the specified category.
    """
    async def get_all_products_by_category(self, filter_key_value:str, limit: int, offset: int):
    
        result = await self.manager.get_all_many_to_many_paginated(
            many_to_many_gem=_product_categories_gem,
            second_table_gem=_categories_gem,
            filter_key_value=filter_key_value, #el valor del id de la categoria
            limit=limit,
            offset=offset
        )      

        return result     
    
    async def get_products_by_name_like(
            self, 
            key_value:str,
            limit:int, 
            offset:int
        ):

        field_key_name = "name"

        result = await self.manager.get_all_paginated_like(
            field_key_name=field_key_name,
            key_value=key_value,
            limit=limit,
            offset=offset
        )

        return result 


    async def get_product_by_id_all_details(self, product_id:str):

        result = await self.manager.get_product_by_id(product_id)

        return result 