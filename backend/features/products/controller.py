
from fastapi import HTTPException, status
from typing import List
from entities.product import Product, ProductApiResponse, ProductAllDetails, ProductAllDetailsWithImages, Pagination
from .service import ProductService

def format_dict_to_pydancti_model(pydantic_model, data:list[dict]) -> list[dict]: 

    result: list = [pydantic_model(**item) for item in data]

    return result

class ProductController:

    def __init__(self, service:ProductService):
        self.service = service
    
    async def get_all(self, limit:int, offset:int) -> ProductApiResponse:

        response_from_service:dict = await self.service.get_all_products(limit,offset)

        # Instanciamos el objeto Pagination directamente desde la clave 'info'
        pagination: Pagination = Pagination(**response_from_service['info'])

        # La lógica de los productos ya está bien, pero ahora usa la clave 'data'
        products:list[ProductAllDetails] = format_dict_to_pydancti_model(ProductAllDetails, response_from_service['data'])
        return ProductApiResponse(info=pagination, data=products)

    
    
    async def get_by_id(self, product_id: str) -> Product:
        
        response_from_service:dict = await self.service.get_by_id(product_id)

        # La lógica de los productos ya está bien, pero ahora usa la clave 'data'
        product:ProductAllDetailsWithImages = response_from_service
        
        return product
    
    async def get_product_by_id_all_details(self, product_id: str) -> ProductAllDetails:
        product_vanilla = await self.service.get_product_by_id_all_details(product_id)

        if not product_vanilla:
                raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"id '{product_id}' not found."
            )

        return product_vanilla
    
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
    ):

        result = await self.service.get_all_products_by_name_like(
            key_value=key_value,
            limit=limit,
            offset=offset
        )
        
        # Instanciamos el objeto Pagination directamente desde la clave 'info'
        pagination: Pagination = Pagination(**result['info'])

        # La lógica de los productos ya está bien, pero ahora usa la clave 'data'
        products:list[ProductAllDetails] = format_dict_to_pydancti_model(ProductAllDetails, result['data'])
        return ProductApiResponse(info=pagination, data=products)
    

         