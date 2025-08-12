from entities.users import User
from fastapi.testclient import TestClient

def test_login(api_client: TestClient):
    """
    Una prueba end-to-end que usa el cliente de prueba.
    """
    data = {
        "username":"admin",
        "password":"123456789",
        "is_admin":True
    }

    response = api_client.post(f"/auth/login/", json=data)
    
    # 2. Verifica el estado de la respuesta
    assert response.status_code == 200
    
    # 3. Obtiene los datos JSON de la respuesta
    response_data = response.json()
    
    # # Aquí puedes hacer tus aserciones
    # assert response_data.username == "admin"
    # assert response_data.is_admin is True
