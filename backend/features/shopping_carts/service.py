from typing import List, Optional

from entities.shopping_cart import ShoppingCart, ShoppingCartItem
from features.shopping_carts.repository import ShoppingCartRepository
from .repository import ShoppingCartRepository

class ShoppingCartService:
    def __init__(self, repository:ShoppingCartRepository):
        self.repository = repository


    async def insert_product_on_cart(self, data: ShoppingCartItem) -> bool:
        
        return await self.repository.insert_product_on_shopping_cart(data)
    
    async def get_cart_items_by_id(self, cart_id:str)-> list[ShoppingCartItem]:
 
        result = await self.repository.get_cart_items(cart_id)

        
        # como se supone que ese metodo del repositorio trae una lista de items y solo
        # deberia de devolver uno, entonces vamos a retornar al controllador solo el prime resultado que se supone debe de ser el unico. 

        return result
      

    async def get_shopping_cart_by_user_id(self, user_id:str)-> ShoppingCart:

        result = await self.repository.get_all_by_user_id(user_id)
        # como se supone que ese metodo del repositorio trae una lista de items y solo
        # deberia de devolver uno, entonces vamos a retornar al controllador solo el prime resultado que se supone debe de ser el unico. 

        return result
      

