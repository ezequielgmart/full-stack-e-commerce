
# from pygem.main import SingleQueries
# from pygem.pydantic_models import Field
# from pygem.queries_generator import Query 
# from entities.migrations import _users_gem, _profiles_gem, _products_gem, _products_inventory_gem, _product_categories_gem, _categories_gem, _product_images_gem, _images_gem


# # def test_select(): 

# #     query_manager = Query()

# #     query_string = query_manager.generate(
# #         gem=_users_gem,
# #         type="SELECT", 
# #         where="username",
# #         limit=False,
# #         offset=False
# #     )

# #     assert query_string == "SELECT user_id, username, email, password, is_admin FROM users WHERE username = $1"

# # def test_select_by_key(): 

# #     schema_entity = SingleQueries(_users_gem)

# #     query_string = schema_entity.select_username_login()

# #     assert query_string == "SELECT user_id, username, email, password, is_admin FROM users WHERE username = $1"
    
# # def test_select_without_where(): 

# #     query_manager = Query()

# #     query_string = query_manager.generate(
# #         gem=_users_gem,
# #         type="SELECT",
# #         limit=False,
# #         offset=False
# #     )

# #     assert query_string == "SELECT user_id, username, email, password, is_admin FROM users"

# # # esta deberia de devolverme el string para seleccionar la informacion de un perfil de acuerdo al id del usuario linkeado. 
# # # 
# # def test_select_profile_join_user():

# #     query_manager = Query()     

# #     query = query_manager.generate_join(
# #         main_gem=_users_gem,
# #         main_fields=["username", "email"],
# #         join_gems=[
# #             {"gem":_profiles_gem, "fields":['first_name','last_name','gender'], "on_key":"user_id", "on_with":"user_id"}
# #         ],
# #         where_field="user_id"
# #     )

# #     expected_query = (
# #         f"SELECT u.username, u.email, p.first_name, p.last_name, p.gender "
# #         f"FROM users AS u JOIN profiles AS p ON u.user_id = p.user_id WHERE "
# #         f"u.user_id = $1"    
# #     )

# #     assert query == expected_query
# # # esto deberia retornar el stock de los productos
# # def test_select_products_join_inventory():

# #     query_manager = Query()     

# #     query = query_manager.generate_join(
# #         main_gem=_products_gem,
# #         main_fields=[
# #             "product_id",
# #             "name",
# #             "description",
# #             "unit_price"
# #             ],
# #         join_gems=[
# #             {"gem":_products_inventory_gem, "fields":["stock"], "on_key":"product_id", "on_with":"product_id"}
# #             ],
# #         where_field="product_id"

# #     )

    
# #     expected_query = (
# #         f"SELECT p.product_id, p.name, p.description, p.unit_price, pi.stock "
# #         f"FROM products AS p "
# #         f"JOIN products_inventory AS pi ON p.product_id = pi.product_id "
# #         f"WHERE p.product_id = $1"

# #     )

# #     assert query == expected_query

# #     # esto deberia retornar el stock de los productos
# # def test_select_products_join_stock_and_category():

# #     products = {"gem":_products_inventory_gem, "fields":["stock"], "on_key":"product_id", "on_with":"product_id"}
# #     products_categories = {"gem":_product_categories_gem, "fields":["category_id"], "on_key":"product_id", "on_with":"product_id"}
# #     categories = {"gem":_categories_gem, "fields":["name"], "on_key":"category_id", "on_with":"category_id"}

# #     query_manager = Query()     

# #     query = query_manager.generate_join(
# #         main_gem=_products_gem,
# #         main_fields=[
# #             "product_id",
# #             "name",
# #             "description",
# #             "unit_price"
# #             ],
# #         join_gems=[
# #             products,
# #             products_categories,
# #             categories
# #         ],
# #         where_field="product_id"

# #     )

# #     expected_query = (
# #         f"SELECT p.product_id, p.name, p.description, p.unit_price, pi.stock, pc.category_id, c.name "
# #         f"FROM products AS p "
# #         f"JOIN products_inventory AS pi ON p.product_id = pi.product_id "
# #         f"JOIN product_categories AS pc ON pi.product_id = pc.product_id " 
# #         f"JOIN categories AS c ON pc.category_id = c.category_id "
# #         f"WHERE p.product_id = $1"
# #     )

# #     assert query == expected_query

# def test_select_products_all_info():

#     products_inventory = {
#         "gem":_products_inventory_gem, 
#         "fields":["stock"], 
#         "on_key":"product_id", 
#         "on_with":"product_id"
#     }

#     products_categories = {
#         "gem":_product_categories_gem, 
#         "fields":["category_id"], 
#         "on_key":"product_id", 
#         "on_with":"product_id"
#     }

#     categories = {
#         "gem":_categories_gem, 
#         "fields":["name"], 
#         "on_key":"category_id", 
#         "on_with":"category_id"
#     }
    
#     images = {
#         "gem":_images_gem, 
#         "fields":["image_url"], # <-- Campo correcto para la URL de la imagen
#         "on_key":"image_id",  # <-- Correcto
#         "on_with":"image_id"  # <-- Correcto
#     }

#     products_images = {
#         "gem":_product_images_gem, 
#         "fields":[], # No necesitamos campos de esta tabla
#         "on_key":"product_id", # <-- Correcto
#         "on_with":"product_id" # <-- Correcto
#     }


#     query_manager = Query()     

#     query = query_manager.generate_join(
#         main_gem=_products_gem,
#         main_fields=[
#             "product_id",
#             "name",
#             "description",
#             "unit_price"
#             ],
#         join_gems=[
#             products_inventory,
#             products_categories,
#             categories,
#             products_images, # <-- ¡Esta debe ir antes de images!
#             images,
#         ],
#         where_field=False

#     )

#     expected_query = (
#         f"SELECT products.product_id, products.name, products.description, products.unit_price, "
#         f"products_inventory.stock, categories.name, "
#         f"ARRAY_AGG(DISTINCT images.image_url) AS image_urls "
#         f"FROM products AS products "
#         f"LEFT JOIN products_inventory AS products_inventory ON products.product_id = products_inventory.product_id "
#         f"LEFT JOIN product_categories AS product_categories ON products.product_id = product_categories.product_id "
#         f"LEFT JOIN categories AS categories ON product_categories.category_id = categories.category_id "
#         f"LEFT JOIN product_images AS product_images ON products.product_id = product_images.product_id "
#         f"LEFT JOIN images AS images ON product_images.image_id = images.image_id "
#     )

#     assert query == expected_query
