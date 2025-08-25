# # backend/tests/test_orders.py

# from backend.entities.migrations import _products_gem
# from backend.config.connect import create_db_pool

# import pytest
# from httpx import AsyncClient

# @pytest.mark.asyncio
# async def test_create_order(api_client: AsyncClient):
#     # Inicializamos 'pool' a None para el bloque 'finally'
#     pool = None
    
#     # Datos de prueba para la orden
#     data = [
#         {
#             "product_id": "1b9e2d3f-4a5c-7d8e-8a1b-9e2d3f4a5c7d",
#             "quantity": 1
#         },
#         {
#             "product_id": "1c2d3e4f-5a6b-7c8d-9e0f-a1b2c3d4e5f6",
#             "quantity": 1
#         },
#         {
#             "product_id": "1c2d3e4f-5a6b-7c8d-9e0f-a1b2c3d4e5f7",
#             "quantity": 3
#         }
#     ]
    
#     # Lista de IDs de productos
#     list_of_products_for_order = [
#         "1b9e2d3f-4a5c-7d8e-8a1b-9e2d3f4a5c7d",
#         "1c2d3e4f-5a6b-7c8d-9e0f-a1b2c3d4e5f6",
#         "1c2d3e4f-5a6b-7c8d-9e0f-a1b2c3d4e5f7"
#     ]
    
#     ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MGQwNjFhMy0xZGVjLTRkYWUtYmNhZC0xNTQwYmE1ZDgxYzIiLCJleHAiOjE3NTU1MTAxODN9.coqjCial-93Zg-pAstb0IIYtBtUV4GlQja94cIU2SyU"
#     headers = {
#         "Authorization": f"Bearer {ACCESS_TOKEN}"
#     }

#     try:
#         pool = await create_db_pool()
        
#         # Aquí puedes verificar que la consulta de la base de datos funciona.
#         # No hay necesidad de un 'assert' de cadena, ya que eso no prueba nada útil.
#         # La mejor práctica es verificar el resultado de la consulta.
#         query = _products_gem.queries.select_products_by_its_id_with_stock_query()
#         async with pool.acquire() as conn:
#             records = await conn.fetch(query, list_of_products_for_order)
#             products_from_db = [dict(record) for record in records]
            
#             # Puedes agregar una aserción aquí para asegurar que se obtienen los productos
#             assert len(products_from_db) == len(list_of_products_for_order)

#     except Exception as e:
#         # Si algo falla en la conexión a la DB, la prueba fallará aquí
#         pytest.fail(f"Error during database setup: {e}")
        
#     finally:
#         # El bloque 'finally' se ejecutará haya o no una excepción en el 'try'
#         # Es crucial cerrar la conexión del pool
#         if pool:
#             await pool.close()

#     # --- Lógica de la prueba de API ---
#     # Esta es la parte principal de tu prueba de integración
    
#     order_response = await api_client.post("/orders/", json=data, headers=headers)

#     # Verificaciones de la respuesta de la API
#     assert order_response.status_code == 200
    
#     response_data = order_response.json()
#     assert "order_id" in response_data
#     assert isinstance(response_data["order_id"], str)