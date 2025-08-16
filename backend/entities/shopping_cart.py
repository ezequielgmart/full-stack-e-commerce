import uuid
from datetime import datetime
from pydantic import BaseModel, Field

class ShoppingCart(BaseModel):
    cart_id: uuid.UUID
    user_id: uuid.UUID
    created_at: datetime

class ShoppingCartItem(BaseModel):
    cart_id: uuid.UUID    
    product_id: uuid.UUID
    quantity: int

class InsertProduct(BaseModel):
    product_id: uuid.UUID
    quantity: int

