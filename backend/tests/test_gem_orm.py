from pygem.main import GEM
from pygem.queries import Query, Add, Delete, Update

import pytest
import pytest_asyncio  # ← Importa explícitamente
from config.connect import DB_CONFIG
from entities.models import Product, User, ShoppingCart, ProductInventory, ProductImage, Image, ProductCategory, Category
import uuid
import datetime

class Repository:
    def __init__(self):
        pass

    async def register_user_with_shopping_cart(self, gem, user: dict, conn):
        new_user = User(
            user_id=user["user_id"],
            username=user["username"],
            email=user["email"],
            password=user["password"],
            is_admin=user["is_admin"]
        )

        result = await gem.create(model_object=new_user, conn=conn)
        if not result:
            raise Exception("Failed to register user")

        new_cart_model = ShoppingCart(
            cart_id=uuid.uuid4(),
            user_id=new_user.user_id,
            created_at=datetime.datetime.now()
        )

        cart_result = await gem.create(model_object=new_cart_model, conn=conn)
        if not cart_result:
            raise Exception("Failed to register shopping_cart")

        return result


@pytest_asyncio.fixture(scope="function")
async def gem_session():
    gem = await GEM.start(DB_CONFIG)
    try:
        print("🧹 cleaning tables...")

        # Trunca en orden correcto
        await gem.execute("TRUNCATE TABLE shopping_carts, users RESTART IDENTITY CASCADE")

        # Verificar después

        yield gem
    finally:
        
        print("🧹 Limpiando tablas...")
        
        # Mueve la lógica de limpieza aquí
        # TRUNCATE es rápido y borra todos los datos. RESTART IDENTITY
        # resetea los contadores de secuencia de las IDs.
        await gem.execute("TRUNCATE TABLE shopping_carts, users RESTART IDENTITY CASCADE")

        print("✔ Tablas limpiadas.")
        
        # Cierra el pool de conexiones
        await gem.pool.close()
        print("❌ Conexión a la base de datos cerrada.")


# # # --- TESTS ASINCRONOS (con DB) ---
# @pytest.mark.asyncio
# async def test_get_all(gem_session):
#     query_string = Query(Product).generate()
#     # Ahora devuelve una lista de objetos Product
#     result = await gem_session.get_all(model_cls=Product, query=query_string)

#     assert str(result[0].product_id) == "b30a1c8f-28c0-43f5-a8e9-d757d54402a1"

@pytest.mark.asyncio
async def test_get_all_one_to_one(gem_session):
    query_string = Query(
        Product,
        Product.product_id,
        Product.name,
        Product.description,
        Product.unit_price,
        ProductInventory.stock
    ).array_agg(
        Image,
        Image.image_url, 
        "images"
    ).join(
        ProductInventory, 
        Product.product_id, 
        ProductInventory.product_id
    ).join(
        ProductImage, 
        Product.product_id, 
        ProductImage.product_id
    ).join(
        Image, 
        ProductImage.image_id, 
        Image.image_id, 
        ProductImage
    ).generate()
    # Ahora devuelve una lista de objetos Product
    result = await gem_session.get_all(query=query_string)

    assert isinstance(result[0]['images'], list)
    assert len(result[0]['images']) > 0

@pytest.mark.asyncio
async def test_get_all_products_paginated(gem_session):
    query_string = Query(
        Product,
        Product.product_id,
        Product.name,
        Product.description,
        Product.unit_price,
        ProductInventory.stock
    ).array_agg(
        Image,
        Image.image_url, 
        "images"
    ).join(
        ProductInventory, 
        Product.product_id, 
        ProductInventory.product_id
    ).join(
        ProductImage, 
        Product.product_id, 
        ProductImage.product_id
    ).join(
        Image, 
        ProductImage.image_id, 
        Image.image_id, 
        ProductImage
    ).paginated().generate()
    # Ahora devuelve una lista de objetos Product
    result = await gem_session.get_all(query=query_string, params=[10,0])

    
    assert len(result) > 0
    assert isinstance(result[0]['images'], list)
    assert len(result[0]['images']) > 0

@pytest.mark.asyncio
async def test_functions_get_ilike_paginated(gem_session):
    query_string = Query(
        Product,
        Product.product_id,
        Product.name,
        Product.description,
        Product.unit_price,
        Category.category_name,
        ProductInventory.stock
    ).array_agg(
        Image,
        Image.image_url, 
        "images"
    ).join(
        ProductCategory, 
        Product.product_id, 
        ProductCategory.product_id
    ).join(
        ProductInventory, 
        Product.product_id, 
        ProductInventory.product_id
    ).join(
        ProductImage, 
        Product.product_id, 
        ProductImage.product_id
    ).join(
        Category, 
        ProductCategory.category_id, 
        Category.category_id, 
        ProductCategory
    ).join(
        Image, 
        ProductImage.image_id, 
        Image.image_id, 
        ProductImage
    ).ilike(Product.name).paginated().generate()

    # pagination = await self.gem_session.get_all(query=pg_qry)
    value = "AMD"
    limit = 10
    offset = 0

    data = await gem_session.get_all_ilike(
        query=query_string, 
        keyword=value, 
        limit=limit, 
        offset=offset
    ) 
    
    assert len(data) > 0
    assert value in data[0]['name']
    assert isinstance(data[0]['images'], list)
    assert len(data[0]['images']) > 0
# @pytest.mark.asyncio
# async def test_get_byid_on_one_to_one(gem_session):
#     id = "b30a1c8f-28c0-43f5-a8e9-d757d54402a1"
#     query_string = Query(
#         Product,
#         Product.product_id,
#         Product.name,
#         Product.description,
#         Product.unit_price,
#         ProductInventory.stock
#     ).array_agg(
#         Image,
#         Image.image_url, 
#         "images"
#     ).join(
#         ProductInventory, 
#         Product.product_id, 
#         ProductInventory.product_id
#     ).join(
#         ProductImage, 
#         Product.product_id, 
#         ProductImage.product_id
#     ).join(
#         Image, 
#         ProductImage.image_id, 
#         Image.image_id, 
#         ProductImage
#     ).where(Product.product_id).generate()
#     # Ahora devuelve una lista de objetos Product
#     result = await gem_session.get_one_or_none(model_cls=Product, query=query_string, param=id)

#     assert str(result.product_id) == "b30a1c8f-28c0-43f5-a8e9-d757d54402a1"
#     assert result.stock == 50

# @pytest.mark.asyncio
# async def test_get_byid_funct_on_one_to_one(gem_session):
#     id = "b30a1c8f-28c0-43f5-a8e9-d757d54402a1"
#     query_string = Query(
#         Product,
#         Product.product_id,
#         Product.name,
#         Product.description,
#         Product.unit_price,
#         ProductInventory.stock
#     ).array_agg(
#         Image,
#         Image.image_url, 
#         "images"
#     ).join(
#         ProductInventory, 
#         Product.product_id, 
#         ProductInventory.product_id
#     ).join(
#         ProductImage, 
#         Product.product_id, 
#         ProductImage.product_id
#     ).join(
#         Image, 
#         ProductImage.image_id, 
#         Image.image_id, 
#         ProductImage
#     ).where(Product.product_id).generate()
#     # Ahora devuelve una lista de objetos Product
#     result = await gem_session.get_one_or_none(model_cls=Product, query=query_string, param=id)

#     assert str(result.product_id) == "b30a1c8f-28c0-43f5-a8e9-d757d54402a1"
#     assert result.stock == 50
# """
#     qr_str = Query(
#         Product,
#         Product.product_id,
#         Product.name,
#         Product.unit_price,
#         ProductInventory.stock
#     ).onlink(Product.product_id).join(ProductInventory).generate()
# """

# @pytest.mark.asyncio
# async def test_get_one(gem_session):
#     query_string = Query(
#         Product,
#         Product.product_id,
#         Product.name,
#         Product.description,
#         Product.unit_price
#     ).where(Product.product_id).generate()

#     id = "b30a1c8f-28c0-43f5-a8e9-d757d54402a1"
#     # Devuelve un objeto Product
#     result = await gem_session.get_one_or_none(
#         model_cls=Product,
#         query=query_string, 
#         param=id
#     )
#     # Accede al atributo con '.' en lugar de '[]'
#     assert str(result.product_id) == id


# @pytest.mark.asyncio
# async def test_get_one_with_name(gem_session):
#     query_string = Query(Product).where(Product.name).generate()
#     name = "MacBook Pro 14"
#     # Devuelve un objeto Product
#     result = await gem_session.get_one_or_none(
#         model_cls=Product,
#         query=query_string, 
#         param=name
#     )
#     # Accede al atributo con '.'

# @pytest.mark.asyncio
# async def test_update_user(gem_session):

#     # crear a un usuario
#     new_user = User(
#             user_id=uuid.uuid4(),
#             username="jondoe",
#             email="jondoe@example.com",
#             password="1a5sd45as1f85qw1fc5ac5a1sv5sd4v5zc1v51za.,lsckals,cqoiefvpadscnasic",
#             is_admin=False,
#         )

#     result = await gem_session.create(
#         model_object=new_user, 
#         conn=None
#     )

#     if result:

#         # Genera la cadena de consulta a partir del objeto Delete
#         update_query_string = Update(
#             User,
#             User.username,
#             User.email,
#             User.is_admin
#         ).where(
#             User.user_id
#         ).query()

        
#         user_id = new_user.user_id
#         updated_username = "newJonDoe"
#         updated_email = "doe@example.com"
#         updated_is_admin = True

#         # Los parámetros siempre deben ir en una lista o tupla
#         await gem_session.modify(query=update_query_string, values=[
#             user_id,
#             updated_username,
#             updated_email,
#             updated_is_admin
#         ])
        

#         await gem_session.modify(query=update_query_string, values=[
#                 user_id,
#                 updated_username,
#                 updated_email,
#                 updated_is_admin
#             ])
        
#     get_query = Query(User).where(User.user_id).generate()
    
#     # Devuelve un objeto User
#     updated_user = await gem_session.get_one_or_none(model_cls=User, query=get_query, param=user_id) 
    
#     # Accede a los atributos con '.'
#     assert updated_user.username == updated_username
#     assert updated_user.email == updated_email
#     assert updated_user.is_admin == updated_is_admin

# # # --- PRUEBA DE TRANSACCIÓN ---
# @pytest.mark.asyncio
# async def test_create_user_and_profile_with_transaction(gem_session):
#     new_user_data = {
#         "user_id": uuid.uuid4(),
#         "username": "jondoe",
#         "email": "jondoe@example.com",
#         "password": "1a5sd45as1f85qw1fc5ac5a1sv5sd4v5zc1v51za.,lsckals,cqoiefvpadscnasic",
#         "is_admin": False,
#     }

#     user_created = await gem_session.begin_transaction(
#         lambda conn: Repository().register_user_with_shopping_cart(
#             gem=gem_session,
#             user=new_user_data,
#             conn=conn
#         )
#     )

#     assert user_created is not None


