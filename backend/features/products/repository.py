from entities.models import Product, ProductImage, ProductInventory, Image, ProductCategory, Category
from entities.product import ProductAllDetails,ProductResponse, Pagination
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
            Category.category_name,
            ProductInventory.stock
        ).array_agg(
            Image,
            Image.image_url, 
            "images"
        ).join(
            ProductCategory, 
            Product.product_id, 
            ProductCategory.product_id
        ).join(
            ProductInventory, 
            Product.product_id, 
            ProductInventory.product_id
        ).join(
            ProductImage, 
            Product.product_id, 
            ProductImage.product_id
        ).join(
            Category, 
            ProductCategory.category_id, 
            Category.category_id, 
            ProductCategory
        ).join(
            Image, 
            ProductImage.image_id, 
            Image.image_id, 
            ProductImage
        ).paginated().generate()

        pg_qry = Query(
            Product,
            Product.product_id
        ).count(Product, Product.product_id).generate()

        pagination = await self.gem_session.get_all(query=pg_qry)

        data = await self.gem_session.get_all(query=query_string, params=[limit, offset]) 

        pages_info = self.pagination_info(pagination, limit)
        products = [ProductAllDetails(**item) for item in data]

        return ProductResponse(info=pages_info, data=products)


    def pagination_info(self, pagination_data:dict, limit:int): 

        total_items = len(pagination_data)
        per_page = limit
        total_pages = int(total_items / limit)


        return Pagination(total_items=total_items, total_pages=total_pages, per_page=per_page)

    async def get_all_products_by_name_like(
            self, 
            value:str,
            limit:int, 
            offset:int
        ):
        query_string = Query(
            Product,
            Product.product_id,
            Product.name,
            Product.description,
            Product.unit_price,
            Category.category_name,
            ProductInventory.stock
        ).array_agg(
            Image,
            Image.image_url, 
            "images"
        ).join(
            ProductCategory, 
            Product.product_id, 
            ProductCategory.product_id
        ).join(
            ProductInventory, 
            Product.product_id, 
            ProductInventory.product_id
        ).join(
            ProductImage, 
            Product.product_id, 
            ProductImage.product_id
        ).join(
            Category, 
            ProductCategory.category_id, 
            Category.category_id, 
            ProductCategory
        ).join(
            Image, 
            ProductImage.image_id, 
            Image.image_id, 
            ProductImage
        ).ilike(Product.name).paginated().generate()

        # pagination = await self.gem_session.get_all(query=pg_qry)

        data = await self.gem_session.get_all_ilike(
            query=query_string, 
            keyword=value, 
            limit=limit, 
            offset=offset
        ) 

        total_items = len(data)
        per_page = limit
        total_pages = int(total_items / limit)

        pages_info = Pagination(
            total_items=total_items, 
            per_page=per_page,
            total_pages=total_pages
        )

        products = [ProductAllDetails(**item) for item in data]

        return ProductResponse(info=pages_info, data=products)

    async def get_by_id(
            self, 
            value:str
        ):
        query_string = Query(
            Product,
            Product.product_id,
            Product.name,
            Product.description,
            Product.unit_price,
            Category.category_name,
            ProductInventory.stock
        ).array_agg(
            Image,
            Image.image_url, 
            "images"
        ).join(
            ProductCategory, 
            Product.product_id, 
            ProductCategory.product_id
        ).join(
            ProductInventory, 
            Product.product_id, 
            ProductInventory.product_id
        ).join(
            ProductImage, 
            Product.product_id, 
            ProductImage.product_id
        ).join(
            Category, 
            ProductCategory.category_id, 
            Category.category_id, 
            ProductCategory
        ).join(
            Image, 
            ProductImage.image_id, 
            Image.image_id, 
            ProductImage
        ).where(Product.product_id).generate()

        # pagination = await self.gem_session.get_all(query=pg_qry)

        data = await self.gem_session.get_one_or_none(
            query=query_string, 
            params=[value]
        ) 

        return ProductAllDetails(**data)

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
