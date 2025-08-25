from pygem.main import Query, Add, Delete, Update, Mapper
from entities.models import Product, User, ShoppingCart, ProductInventory, Image, ProductImage
import uuid


def test_select_query():
    query_string = Query(
        Product,
        Product.product_id,
        Product.name,
        Product.description,
        Product.unit_price
    ).generate()
    
    expected_query = "SELECT products.product_id, products.name, products.description, products.unit_price FROM products AS products"
    assert query_string == expected_query

def test_select_all_user_query():
    query_string = Query(User).generate()
    assert query_string == "SELECT users.* FROM users AS users"

def test_select_all_user_query_paginated():
    query_string = Query(User).order_by(User.username).paginated().generate()
    # There was an extra space in the string, which I've removed
    assert query_string == "SELECT users.* FROM users AS users  ORDER BY username LIMIT $1 OFFSET $2"

def test_select_one_to_one():
    qr_str = Query(
        Product,
        Product.product_id,
        Product.name,
        Product.unit_price,
        ProductInventory.stock
    ).join(
        ProductInventory, 
        Product.product_id, 
        ProductInventory.product_id
    ).generate()

    query_to_compare = (
        "SELECT products.product_id, products.name, products.unit_price, products_inventory.stock "
        "FROM products AS products JOIN products_inventory AS products_inventory ON products.product_id = products_inventory.product_id"
    )
    
    assert query_to_compare == qr_str



def test_select_query_with_filter():
    query_string = Query(
        Product,
        Product.product_id,
        Product.name,
        Product.description,
        Product.unit_price
    ).where(Product.product_id).generate()
    
    expected_query = "SELECT products.product_id, products.name, products.description, products.unit_price FROM products AS products  WHERE product_id = $1"
    assert query_string == expected_query
def test_insert_query():
    new_user = User(
        user_id=uuid.uuid4(),
        username="jondoe",
        email="jondoe@example.com",
        password="1a5sd45as1f85qw1fc5ac5a1sv5sd4v5zc1v51za.,lsckals,cqoiefvpadscnasic",
        is_admin=False
    )

    new_product = Product(
        product_id=uuid.uuid4(),
        name="Pato",
        description="producto para identificar que tan pato es gabriel",
        unit_price=2546.00
    )

    user_query = Add(new_user).query()
    product_query = Add(new_product).query()

    assert user_query == "INSERT INTO users (user_id, username, email, password, is_admin) VALUES ($1, $2, $3, $4, $5) RETURNING user_id, username, email, password, is_admin"
    assert product_query == "INSERT INTO products (product_id, name, description, unit_price) VALUES ($1, $2, $3, $4) RETURNING product_id, name, description, unit_price"

def test_delete_query(): 

    query_string = Delete(
        Product
    ).where(Product.product_id).query()

    assert query_string == "DELETE FROM products WHERE product_id = $1"

def test_update_all_fields(): 

    query_string = Update(
        User,
        User.username,
        User.email,
        User.password,
        User.is_admin
    ).where(User.primary_key).query()

    assert query_string == "UPDATE users SET username = $2, email = $3, password = $4, is_admin = $5 WHERE user_id = $1"

def test_functions_get_all_array():
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
    
    expected_query = "SELECT products.product_id, products.name, products.description, products.unit_price, products_inventory.stock, array_agg(images.image_url) AS images FROM products AS products JOIN products_inventory AS products_inventory ON products.product_id = products_inventory.product_id JOIN product_images AS product_images ON products.product_id = product_images.product_id JOIN images AS images ON product_images.image_id = images.image_id GROUP BY products.product_id, products.name, products.description, products.unit_price, products_inventory.stock"
    
    assert query_string == expected_query

def test_functions_array_by_id():
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
    ).where(Product.product_id).generate()
    
    expected_query = "SELECT products.product_id, products.name, products.description, products.unit_price, products_inventory.stock, array_agg(images.image_url) AS images FROM products AS products JOIN products_inventory AS products_inventory ON products.product_id = products_inventory.product_id JOIN product_images AS product_images ON products.product_id = product_images.product_id JOIN images AS images ON product_images.image_id = images.image_id WHERE products.product_id = $1 GROUP BY products.product_id, products.name, products.description, products.unit_price, products_inventory.stock"
    
    assert query_string == expected_query


#     expected_query = """SELECT
#     products.product_id,
#     products.name,
#     products.description,
#     products.unit_price,
#     array_agg(i.image_url) AS images
# FROM
#     products AS p
# JOIN
#     product_images AS pi ON products.product_id = pi.product_id
# JOIN
#     images AS i ON pi.image_id = i.image_id
# GROUP BY
#     products.product_id, products.name, products.description, products.unit_price
# LIMIT 100"""
