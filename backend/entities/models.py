from pygem.schema import *
import uuid 
import datetime

# esta tabla tiene una relacion uno a uno con product debido a que cada product solo puede tener un stock y viceversa 

class ProductInventory(Schema):
    _tablename_ = "products_inventory"

     # product_id es a la vez PK de esta tabla y FK que se conecta a la tabla products
    product_id = ForeignKey(reference="products.product_id", primary_key=True)
    stock = Column(type=int)

# Ejemplo de un modelo final
class Product(Schema):
    _tablename_ = "products" 
    product_id = Column(type=uuid.UUID, primary_key = True)
    name = Column(type=str)
    description = Column(type=str)
    unit_price = Column(type=float)

    # La relación para acceder al inventario desde el producto
    inventory = Relationship(foreign_key_column=ProductInventory.product_id, model=ProductInventory)


class User(Schema):
    _tablename_ = "users"
    user_id = Column(type=uuid.UUID, primary_key = True)
    username = Column(type=str)
    email = Column(type=str)
    password = Column(type=str)
    is_admin = Column(type=bool)

class Profile(Schema):
    _tablename_ = "profiles"
    user_id = Column(type=uuid.UUID, primary_key = True)
    first_name = Column(type=str)
    last_name = Column(type=str)
    gender = Column(type=str)

class ShoppingCart(Schema):
    _tablename_ = "shopping_carts"
    cart_id=Column(type=uuid.UUID, primary_key = True)
    user_id=Column(type=uuid.UUID)
    created_at=Column(type=datetime.datetime)

    
class Image(Schema):
    _tablename_ = "images"
    image_id=Column(type=int, primary_key = True)
    image_url=Column(type=str)

            
class ProductImage(Schema):
    _tablename_ = "product_images"
    product_id=Column(type=uuid.UUID, primary_key = True)
    image_id=Column(type=int)
"""

# Crea un nuevo objeto Producto
new_product = Product(
    product_id=uuid.uuid4(),
    name="Teclado Mecánico",
    description="Teclado de alta calidad para programadores.",
    unit_price=120.50
)

# Agrega el objeto a la sesión. SQLAlchemy lo marcará para una inserción.
session.add(new_product)

# Guarda el cambio en la base de datos (aquí es donde se ejecuta el INSERT)
session.commit()

print(f"Nuevo producto creado con ID: {new_product.product_id}")

# Encuentra el producto que quieres actualizar
product_to_update = session.query(Product).filter_by(name="Teclado Mecánico").one_or_none()

if product_to_update:
    # Modifica los atributos del objeto. La sesión rastrea este cambio.
    product_to_update.unit_price = 140.00
    product_to_update.description = "Nuevo precio para este teclado."

    # Guarda el cambio en la base de datos (aquí se ejecuta el UPDATE)
    session.commit()
    print("Producto actualizado con éxito.")
else:
    print("Producto no encontrado.")

# Encuentra el producto que quieres eliminar
product_to_delete = session.query(Product).filter_by(name="Teclado Mecánico").one_or_none()

if product_to_delete:
    # Le dices a la sesión que este objeto debe ser eliminado
    session.delete(product_to_delete)

    # Guarda el cambio en la base de datos (aquí se ejecuta el DELETE)
    session.commit()
    print("Producto eliminado con éxito.")
else:
    print("Producto no encontrado.")
    
"""    