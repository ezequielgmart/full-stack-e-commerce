from typing import List, Optional
from entities.shopping_cart import ShoppingCart,ShoppingCartItem
from pygem.main import GemRepository
from config.connect import DbPool
from entities.migrations import _shopping_carts_gem, _cart_items_gem

# aqui tengo que utilzizar el schema de la tabla shopping cart item.  

"""

lo hago asi porque shopping-cart-item depende directamente de shopping cart y es 
una tabla simplemente de union para unir productos con carritos. 

"""   
class ShoppingCartItem(GemRepository):

    def __init__(self, pool:DbPool):
        self.gem = _cart_items_gem   
        super().__init__(model=ShoppingCartItem, gem=self.gem, pool=pool)

    async def get_all_items_on_cart(self, cart_id:str) -> list[ShoppingCartItem]:
        field_name = 'cart_id'
        return await self.manager.get_all_by_key(field_name, cart_id)
    
    async def remove_product_from_cart(self, product_id:str, conn) -> bool:

        field_name = 'product_id'

        return await self.manager.delete_by_custom_field_with_transaction(field_name, product_id, conn)



class ShoppingCartRepository(GemRepository):

    def __init__(self, pool:DbPool):
        self.gem = _shopping_carts_gem
        self.cart_item_repo = ShoppingCartItem(pool) # inicializo el shopping cart item para usar su metodo create
        super().__init__(model=ShoppingCart, gem=self.gem, pool=pool)

    async def insert_product_on_shopping_cart(self, data:ShoppingCartItem) -> bool:

        # para evitar que siga retornando un dict, 
        # por el momento pondre que solo vuelva True si se pudo insertar correctamente
        return await self.cart_item_repo.create_no_returning(data)

    async def get_cart_items(self, cart_id:str) -> list[ShoppingCartItem]:

        return await self.cart_item_repo.get_all_items_on_cart(cart_id)

    async def get_cart_by_current_user_id(self, current_user_id: str) -> Optional[ShoppingCart]:
        result = await self.get_all_by_user_id(current_user_id)
        
        # Check if the list is not empty before trying to access the first element.
        if result:
            # We assume the first item is the user's cart.
            return result[0]
        return None # Return None if no cart is found.


    async def remove_product_from_shopping_cart_items(self, product_id:str, conn) -> bool: 

        return await self.cart_item_repo.remove_product_from_cart(product_id, conn)


