from pygem.main import GEM, Query, Add, Delete
import pytest
import pytest_asyncio  # ← Importa explícitamente
from config.connect import DB_CONFIG
from entities.models import Product, User, ShoppingCart
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

        # Verificar conteo antes
        count_users_before = await gem.get_all("SELECT COUNT(*) FROM users")
        count_carts_before = await gem.get_all("SELECT COUNT(*) FROM shopping_carts")
        print(f"Usuarios antes: {count_users_before[0]['count']}, Carritos antes: {count_carts_before[0]['count']}")

        # Trunca en orden correcto
        await gem.execute("TRUNCATE TABLE shopping_carts, users RESTART IDENTITY CASCADE")

        # Verificar después
        count_users_after = await gem.get_all("SELECT COUNT(*) FROM users")
        count_carts_after = await gem.get_all("SELECT COUNT(*) FROM shopping_carts")
        print(f"Usuarios después: {count_users_after[0]['count']}, Carritos después: {count_carts_after[0]['count']}")

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

# --- TESTS UNITARIOS (no necesitan DB) ---
def test_schema_attrs():
    assert Product.product_id.name == "product_id"
    assert Product.name.name == "name"
    assert Product.description.name == "description"
    assert Product.unit_price.name == "unit_price"


def test_select_query():
    query_string = Query(
        Product,
        Product.product_id,
        Product.name,
        Product.description,
        Product.unit_price
    ).generate()

    assert query_string == "SELECT product_id, name, description, unit_price FROM products "


def test_select_all_user_query():
    query_string = Query(User).generate()
    assert query_string == "SELECT * FROM users "


def test_select_query_with_filter():
    query_string = Query(
        Product,
        Product.product_id,
        Product.name,
        Product.description,
        Product.unit_price
    ).add_filter(Product.product_id).generate()

    assert query_string == "SELECT product_id, name, description, unit_price FROM products WHERE product_id = $1"


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
    ).add_clause(Product.product_id).query()

    assert query_string == "DELETE FROM products WHERE product_id = $1"



# --- TESTS ASINCRONOS (con DB) ---
@pytest.mark.asyncio
async def test_get_all(gem_session):  # ✅ Inyecta la fixture
    query_string = Query(Product).generate()
    result = await gem_session.get_all(query_string)
    assert str(result[0]["product_id"]) == "b30a1c8f-28c0-43f5-a8e9-d757d54402a1"


@pytest.mark.asyncio
async def test_get_one(gem_session):
    query_string = Query(
        Product,
        Product.product_id,
        Product.name,
        Product.description,
        Product.unit_price
    ).add_filter(Product.product_id).generate()

    id = "b30a1c8f-28c0-43f5-a8e9-d757d54402a1"
    result = await gem_session.get_one_or_none(query=query_string, param=id)
    assert str(result["product_id"]) == id


@pytest.mark.asyncio
async def test_get_one_with_name(gem_session):
    query_string = Query(Product).add_filter(Product.name).generate()
    name = "MacBook Pro 14"
    result = await gem_session.get_one_or_none(query=query_string, param=name)
    assert result["name"] == name


@pytest.mark.asyncio
async def test_get_one_wrong_id(gem_session):
    query_string = Query(
        Product,
        Product.product_id,
        Product.name,
        Product.description,
        Product.unit_price
    ).add_filter(Product.product_id).generate()

    id = "b30a1c8f-28c0-43f5-a8e9-d757d54402aa"
    result = await gem_session.get_one_or_none(query=query_string, param=id)
    assert result is None

@pytest.mark.asyncio
async def test_delete_user(gem_session):

    # crear a un usuario
    new_user = User(
            user_id=uuid.uuid4(),
            username="jondoe",
            email="jondoe@example.com",
            password="1a5sd45as1f85qw1fc5ac5a1sv5sd4v5zc1v51za.,lsckals,cqoiefvpadscnasic",
            is_admin=False,
        )

    result = await gem_session.create(
        model_object=new_user, 
        conn=None
    )

    if result:

        # Genera la cadena de consulta a partir del objeto Delete
        delete_query_string = Delete(User).add_clause(User.user_id).query()
        user_id_param = new_user.user_id
        # Los parámetros siempre deben ir en una lista o tupla
        rows_affected = await gem_session.remove(query=delete_query_string, param=[user_id_param])
    
    assert rows_affected == True


# --- PRUEBA DE TRANSACCIÓN ---
@pytest.mark.asyncio
async def test_create_user_and_profile_with_transaction(gem_session):
    new_user_data = {
        "user_id": uuid.uuid4(),
        "username": "jondoe",
        "email": "jondoe@example.com",
        "password": "1a5sd45as1f85qw1fc5ac5a1sv5sd4v5zc1v51za.,lsckals,cqoiefvpadscnasic",
        "is_admin": False,
    }

    user_created = await gem_session.begin_transaction(
        lambda conn: Repository().register_user_with_shopping_cart(
            gem=gem_session,
            user=new_user_data,
            conn=conn
        )
    )

    assert user_created is not None


    user_from_db = await gem_session.get_one_or_none(
        "SELECT * FROM users WHERE user_id = $1",
        str(new_user_data["user_id"])
    )
    assert user_from_db is not None

