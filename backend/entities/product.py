import uuid 
from pydantic import BaseModel
from entities.pagination import Pagination

class Product(BaseModel):

    product_id: uuid.UUID
    name: str
    description:str
    unit_price:float
    
    # Nuevo en Pydantic v2: Configuración para manejar tipos arbitrarios
    class ConfigDict:
        arbitrary_types_allowed = True

class ProductRequest(BaseModel):

    name: str
    description: str
    unit_price: float    


class ProductAllDetails(BaseModel):

    product_id: uuid.UUID
    name: str
    description:str
    unit_price:float
    stock:int
    category_name:str
    images:list

class ProductResponse(BaseModel):

    info:Pagination
    data:list[ProductAllDetails]   