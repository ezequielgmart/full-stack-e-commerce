from entities.models import Product, ProductImage, ProductInventory, Image, ProductCategory, Category
from pygem.queries import Query, GetPagination


class ProductRepository():

    def __init__(self, gem_session):
        self.gem_session = gem_session


    """
        @method: Retrieves a paginated list of products belonging to a specific category.
        
        This method uses a many-to-many relationship to find all products
        linked to a given category ID, applying pagination to the results, 
        however it was change to return only the cover photo of the product.
        
        @params:
            - filter_key_value (str): The UUID of the category to filter by.
            - limit (int): The maximum number of products to return in the current page.
            - offset (int): The number of products to skip from the beginning of the result set.
            
        @return:
            - List[Dict[str, Any]] | None: A list of dictionaries representing the products,
              or None if no products are found for the specified category.
    """
    async def get_all_products(self, limit: int, offset: int) -> list[dict]:
    
        query_string = Query(
            Product,
            Product.product_id,
            Product.name,
            Product.description,
            Product.unit_price,
            Category.category_name,
            ProductInventory.stock,
            Image.image_url
        ).left_join(
            ProductCategory, 
            Product.product_id, 
            ProductCategory.product_id
        ).left_join(
            ProductInventory, 
            Product.product_id, 
            ProductInventory.product_id
        ).left_join(
            ProductImage, 
            Product.product_id, 
            ProductImage.product_id
        ).left_join(
            Category, 
            ProductCategory.category_id, 
            Category.category_id, 
            ProductCategory
        ).left_join(
            Image, 
            ProductImage.image_id, 
            Image.image_id, 
            ProductImage
        ).where(ProductImage, ProductImage.is_cover).paginated().generate()


        data = await self.gem_session.get_all(query=query_string, params=[True, limit, offset]) 


        """ 
        
        NOTA PARA TI DEL FUTURO

        apartir de ahora (9/5/25) las capas service y repository seran agnosticas de la validacion de pydantic y fast api. 

        esto como medida de evitar una dependencia / repsonsabilidad de algo que no es su responsabilidad principal. La capa repository solo se encarga de guardar o recibir datos, validar que sean datos confaibles y veridicos, mas no de prepararlos para el frontend. La capa encargada de eso sera el controlador, porque de ese modo, le dejo la tarea a la unica capa que esta relacioanda con el framework que estoy utilzando para la api rest, asi si necesito utilizar la capa de serivicos para una posterior integracion con uina aplicacion de admin no necesito que siga las validaciones de los modelos pydantic, puedo trabajar con una lista de diccionarios.  
        

        ahora esta funcion retorna una lista (response: list)

        **** pagination_info: para la paginacion
        **** data: la informacion recibida de la bd transformada en dictionarios. 

        """
        
        pagination_info = await self.pagination_info(limit)
        # total_items = len(data)

        response = {
            "info":pagination_info,
            "data":data
            
        }

        return response 


    # esto devuelve un dictionario con la informacion de la paginacion
    async def pagination_info(self, limit:int, count_item_total=None): 

        pagination_generator:object = GetPagination()

        pagination_info = await pagination_generator.get_pagination_info(
            gem_session=self.gem_session,
            model=Product,
            field=Product.product_id,
            limit=limit,
            count_item_total=count_item_total
        )


        return pagination_info
        # Consulta para contar cuantos 
        # pg_qry = Query(
        #     Product,
        #     Product.product_id
        # ).count(Product, Product.product_id).generate()

        # count_total_from_db = await self.gem_session.get_all(query=pg_qry)

        # total_items = len(count_total_from_db)
        # per_page = limit
        # total_pages = int(total_items / limit)

        # pagination = {
        #     "total_items":total_items,
        #     "per_page":per_page,
        #     "total_pages":total_pages,
        # }

        # return pagination


        # return Pagination(total_items=total_items, total_pages=total_pages, per_page=per_page)

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
            ProductInventory.stock,
            Image.image_url
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
        ).where(ProductImage, ProductImage.is_cover).ilike(Product, Product.name).paginated().generate()

        # pagination = await self.gem_session.get_all(query=pg_qry)

        data = await self.gem_session.get_all_ilike(
            where_clause_value=True, # para decirle que la condicion del WHERE es que sea TRUE
            query=query_string, 
            keyword=value, 
            limit=limit, 
            offset=offset
        ) 

        total_items = len(data)

        pagination:dict = {
                "total_items":total_items,
                "per_page":limit,
                "total_pages":int(total_items / limit),
            }
        
        response = {
            "info":pagination,
            "data":data
            
        }

        return response 
    
        # products = [ProductAllDetailsWithImages(**item) for item in data]

        # return ProductResponse(info=pages_info, data=products)

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
        ).where(Product, Product.product_id).generate()

        # pagination = await self.gem_session.get_all(query=pg_qry)

        # esto no trae una lista, trae un solo objeto
        response = await self.gem_session.get_one_or_none(
            query=query_string, 
            params=[value]
        ) 

        return response 

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
