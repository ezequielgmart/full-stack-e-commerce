import uuid
import datetime
from typing import List, Dict, Any

from pydantic import BaseModel

# Tus imports originales
from entities.orders import Order, OrderRegister, OrderItem, OrderItemRegister, OrderWithItems
from pygem.main import GemRepository
from config.connect import DbPool
from features.products.repository import ProductRepository
from features.shopping_carts.repository import ShoppingCartRepository
from entities.migrations import _orders_gem, _order_items_gem


# Los comentarios originales del usuario están entre comillas dobles.
class OrderItemsRepository(GemRepository):
    
    def __init__(self, pool: DbPool):
        self.gem = _order_items_gem
        super().__init__(model=OrderItem, gem=self.gem, pool=pool)

    # get all the items that belongs to a order by this order_id
    async def get_order_items_by_id(self, order_id: str):
        pass

    # insert product on a order list of items
    # this will be called on the purchase process
    async def insert_product_on_order_items(self, order_item_model: OrderItem, conn):
        """
        Inserta un item de orden de forma atómica en una transacción.
        """
        return await self.create_with_transaction(data=order_item_model.model_dump(), conn=conn)


class OrderRepository(GemRepository):
    
    def __init__(self, pool: DbPool):
        self.gem = _orders_gem
        self.products_repo = ProductRepository(pool)
        self.order_items_repo = OrderItemsRepository(pool)
        self.shopping_cart_repo = ShoppingCartRepository(pool)
        super().__init__(model=Order, gem=self.gem, pool=pool)

    async def get_order_by_id(self, order_id:str) -> OrderWithItems:
        pass
        # return await self.get_order_by_id()

    # this method will be called on the new_order service.
    # Se ha corregido el tipo de 'user_id' y el tipo de 'order_register'
    # TODO: debo de modular esta funcion en pequeñas funciones para que sea mas facil de mantener. 
    async def create_order(self, user_id: uuid.UUID, list_of_items: list[OrderItemRegister]) -> str:
        """
        Procesa una orden de compra de forma atómica.
        
        Abre una transacción para:
        1. Validar el inventario de todos los productos en la orden.
        2. Calcular el costo total y los impuestos.
        3. Crear un registro en la tabla de órdenes.
        4. Insertar cada producto en la tabla de items de la orden.
        5. Actualizar el inventario de los productos comprados.
        6. Eliminar los productos del carrito del usuario.
        
        Args:
            user_id (uuid.UUID): El ID del usuario que crea la orden.
            list_of_items (list[OrderItemRegister]): La lista de productos y cantidades.
        
        Returns:
            str: El ID de la nueva orden si la transacción es exitosa.
        
        Raises:
            ValueError: Si un producto no tiene suficiente stock o si no es encontrado.
        """
        # "abrir un pool para la transaccion:"
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                # "VALIDAR INVENTARIO"
                # "comprobar que tenemos = o + cantidad del stock que esta pidiendo la orden"
                
                # Obtenemos los IDs de los productos de la orden directamente de la lista.
                product_ids = [item.product_id for item in list_of_items]
                
                # Resuelve el problema N+1: una sola consulta para todos los productos.
                # Pasar la conexión de la transacción al método del repositorio.
                products_from_db = await self.products_repo.get_products_by_ids_with_transaction(product_ids, conn)
                
                
                # Creamos un diccionario para un acceso rápido y eficiente a la información del producto.
                products_map = {str(p['product_id']): p for p in products_from_db}
                
                cost_total = 0.0

                # 1. Validar inventario y calcular el costo total en un solo bucle.
                for item in list_of_items:
                    product_id_str = str(item.product_id)
                    
                    if product_id_str not in products_map:
                        raise ValueError(f"Product with ID {product_id_str} not found.")
                    
                    product_data = products_map[product_id_str]
                    
                    # Validación del stock
                    if item.quantity > product_data['stock'] or product_data['stock'] == 0:
                        raise ValueError(f"Insufficient stock for product {product_id_str}.")
                    
                    # Calcular el costo total usando el precio de la base de datos (seguro).
                    cost_total += item.quantity * float(product_data['unit_price'])

                # 2. Calcular impuestos y generar el ID de la orden.
                # "calcular el sale_tax (18% del costo total)"
                sales_tax_amount = cost_total * 0.18
                order_id = uuid.uuid4()
                
                # 3. Crear la orden principal en la base de datos.
                order_data = { 
                    "order_id":order_id,
                    "user_id":user_id,
                    "status_id":1,
                    "cost_total":cost_total,
                    "sales_tax":sales_tax_amount,
                    "created_at":datetime.datetime.now()
                }
       
                
                # Pasar el diccionario de la orden al método de la base de datos.
                await self.create_with_transaction(data=order_data, conn=conn)

                # 4. Llenar la tabla de items de la orden y actualizar el inventario.
                for item in list_of_items:
                    # Crear el registro del item en la orden
                    order_item_model = OrderItem(
                        order_id=order_id,
                        product_id=item.product_id,
                        quantity=item.quantity
                    )
                    # El método insert_product_on_order_items ya maneja la conversión a diccionario.
                    await self.order_items_repo.insert_product_on_order_items(order_item_model, conn)

                    # **Paso crucial: Actualizar el inventario**
                    # Nota: Debes implementar este método en tu ProductRepository
                    # await self.products_repo.update_stock_with_transaction(item.product_id, -item.quantity, conn)
                    
                    # **Paso crucial: Eliminar el producto del carrito del usuario**
                    # Nota: Debes implementar este método en tu ShoppingCartRepository
                    item_for_removing = item.product_id
                    await self.shopping_cart_repo.remove_product_from_shopping_cart_items(item_for_removing, conn)

                # "Confirma la transacción: Si todo va bien, se confirma la transacción."
                # El bloque `async with conn.transaction():` confirma la transacción automáticamente
                # cuando la ejecución llega a este punto sin errores.
                return str(order_id)
            