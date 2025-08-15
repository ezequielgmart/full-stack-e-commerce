import uuid 
from pydantic import BaseModel

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


class ProductCategoryStock(BaseModel):

    product_id: uuid.UUID
    name: str
    description:str
    unit_price:float
    stock:int
    category_id:uuid.UUID
    category_name:str

   