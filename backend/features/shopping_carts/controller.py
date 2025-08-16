from fastapi import HTTPException, status
from typing import Optional
from entities.shopping_cart import ShoppingCart, ShoppingCartItem, InsertProduct
from .service import ShoppingCartService


class ShoppingCartController:

    def __init__(self, service:ShoppingCartService):
        self.service = service

    async def insert_product_on_cart(self, user_id:str, product_to_insert:InsertProduct) -> Optional[ShoppingCartItem]:
        
        result = await self.get_cart_by_current_user_id(user_id)
        
        current_usert_cart = result[0]
       
        new_product_on_card = ShoppingCartItem(
            cart_id=current_usert_cart.cart_id,
            product_id=product_to_insert.product_id,
            quantity=product_to_insert.quantity
        )
        
        result = await self.service.insert_product_on_cart(new_product_on_card)
        
        if not result: 
            # if something fail trying to insert the users_cart it'll create a automatic rollback 
            raise Exception("Failed inserting product on cart")
        
        return result
    
    async def get_all_cart_items(self, user_id:str):
        
        result = await self.get_cart_by_current_user_id(user_id)
        current_usert_cart = result[0]

        cart_id = current_usert_cart.cart_id


        return await self.service.get_cart_items_by_id(cart_id)
    
    # esto debe de traerme la informacion del carrito del usuario que esta logueado para asi 
    # evitar mandar el cart_id por la url
    async def get_cart_by_current_user_id(self, current_user_id:str) -> ShoppingCart:

        result = await self.service.get_shopping_cart_by_user_id(current_user_id) 

        return result