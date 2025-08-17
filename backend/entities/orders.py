
import uuid 
from pydantic import BaseModel
from datetime import datetime

class Order(BaseModel):

    order_id:uuid.UUID
    user_id:uuid.UUID
    status_id:int
    cost_total:float
    sales_tax:float
    created_at:datetime
  
class OrderItem(BaseModel):
    
    order_id:uuid.UUID
    product_id:uuid.UUID
    quantity:int

class OrderItemRegister(BaseModel): 
    
    product_id:uuid.UUID
    quantity:int

class OrderRegisterNoUser(BaseModel):

    list_of_items:list[OrderItem]


class OrderRegister(BaseModel):

    user_id:uuid.UUID
    status_id:int
    created_at:datetime
    list_of_items:list[OrderItem]

class OrderWithItems:
    
    order_id:uuid.UUID
    user_id:uuid.UUID
    status_id:int
    cost_total:float
    sales_tax:float
    created_at:datetime    
    list_of_items:list[OrderItem]
