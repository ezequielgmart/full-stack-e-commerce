from entities.models import Product, ProductImage, ProductInventory, Image
from pygem.main import GEM
from pygem.queries import Query


class ProductRepository():

    def __init__(self, gem_session):
        self.gem_session = gem_session

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
    async def get_all_products(self, limit: int, offset: int):
    
        query_string = Query(
            Product,
            Product.product_id,
            Product.name,
            Product.description,
            Product.unit_price,
            ProductInventory.stock
        ).array_agg(
            Image,
            Image.image_url, 
            "images"
        ).join(
            ProductInventory, 
            Product.product_id, 
            ProductInventory.product_id
        ).join(
            ProductImage, 
            Product.product_id, 
            ProductImage.product_id
        ).join(
            Image, 
            ProductImage.image_id, 
            Image.image_id, 
            ProductImage
        ).paginated().generate()

        result = await self.gem_session.get_all(model_cls=Product, query=query_string, params=[limit, offset]) 

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

    
    """
    # obtiene la info de todos los productos de golpe en lugar de 
    # hacer varias consultas al a db
    # para mas referencia: 

    El problema de N+1
        Imagina que tienes 10 productos en el carrito.

        Tu código actual hace esto:

        Obtener el producto 1.

        Obtener el producto 2.

        Obtener el producto 3.
        ...

        Obtener el producto 10.

        Eso significa que tu aplicación hace 10 consultas 
        a la base de datos (N consultas) además de la consulta original (1)
        para obtener el carrito. En total, serían 1 + N consultas. 
        Por eso se llama el problema de N+1. Esto crea una carga innecesaria 
        en la base de datos y aumenta la latencia de tu aplicación, 
        lo cual se vuelve muy notable con muchos usuarios.
    """
    # TODO
    # async def get_products_by_ids_with_transaction(self, product_ids: list[str], conn) -> list:

    #     result = await self.manager.get_items_by_ids_with_transaction(product_ids, conn)

    #     return result

    async def get_product_by_id_all_details(self, product_id:str):

        result = await self.manager.get_product_by_id(product_id)

        return result 