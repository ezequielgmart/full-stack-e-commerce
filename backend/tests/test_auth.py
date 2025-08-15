from entities.users import User
from fastapi import HTTPException, status
from fastapi.testclient import TestClient

TEST_ID = "b370a256-4b9e-4b2a-a9e9-7d54d7502b14"
TEST_USER = "admin"
TEST_PASSWORD = "123456789"
TEST_IS_ADMIN = True


def test_login(api_client: TestClient):
    """
    Una prueba end-to-end que usa el cliente de prueba.
    """
    data = {
        "username":TEST_USER,
        "password":TEST_PASSWORD,
        "is_admin":TEST_IS_ADMIN
    }

    response = api_client.post(f"/auth/login/", json=data)
    
    # 2. Verifica el estado de la respuesta
    assert response.status_code == 200
    
    # 3. Obtiene los datos JSON de la respuesta
    response_data = response.json()
    
    # # Aquí puedes hacer tus aserciones
    # assert response_data.username == "admin"
    # assert response_data.is_admin is True

def test_get_protected_user_profile(api_client: TestClient):
    """
    Prueba end-to-end para una ruta protegida.
    """
    # 1. Autenticarse para obtener el token
    login_data = {
        "username": TEST_USER,
        "password": TEST_PASSWORD,
        "is_admin": TEST_IS_ADMIN
    }
    
    login_response = api_client.post("auth/login", json=login_data)
    
    # Asegurarse de que el login fue exitoso
    assert login_response.status_code == 200
    
    # 2. Extraer el token del cuerpo de la respuesta
    token_data = login_response.json()
    access_token = token_data.get("access_token")
    
    # Verificar que recibimos el token
    assert access_token is not None
    
    # 3. Crear el encabezado de autorización
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    # 4. Hacer la petición GET a la ruta protegida con el token en el encabezado
    # Asume que la ruta protegida es "/users/me" y que no requiere user_id.
    protected_response = api_client.get("auth/public", headers=headers)
    
    # 5. Verificar el estado de la respuesta y el contenido
    assert protected_response.status_code == 200
    
    protected_result = protected_response.json()
    
    # Verificar que la respuesta contiene los datos correctos del usuario logueado

    assert protected_result["username"] == TEST_USER
    assert protected_result["is_admin"] == TEST_IS_ADMIN

# --- Un test adicional para verificar que la ruta está protegida ---

def test_protected_route_without_token(api_client: TestClient):
    """
    Verifica que la ruta protegida devuelve 401 si no hay token.
    """
    response = api_client.get("auth/public")
    assert response.status_code == 401
    assert "detail" in response.json()
    assert response.json()["detail"] == "Not authenticated"
