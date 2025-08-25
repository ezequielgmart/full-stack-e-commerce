# # backend/tests/test_search.py

# from fastapi.testclient import TestClient

# def test_search_products_by_name(api_client: TestClient):
#     """
#     Una prueba end-to-end que usa el cliente de prueba.
#     """
#     key_word = "AMD"
#     response = api_client.get(f"/products/search/{key_word}?limit=5")
    
#     # Aquí puedes hacer tus aserciones
#     assert response.status_code == 200
#     assert len(response.json()) > 0
#     assert "AMD" in response.json()[0]["name"]

# def test_get_by_category_id(api_client: TestClient):
#     category_id = 'b30a1c8f-28c0-43f5-a8e9-d757d54403c1'
#     response = api_client.get(f"/products/all/{category_id}?limit=10")

#     assert response.status_code == 200
#     assert len(response.json()) == 10


# def test_get_product_by_id(api_client: TestClient):

#     product_id = '2a4b6c8d-0e1f-2a3b-4c5d-6e7f8a9b0c1d'
#     response = api_client.get(f"/products/{product_id}")
    
#     assert response.status_code == 200
#     assert response.json()["product_id"] == "2a4b6c8d-0e1f-2a3b-4c5d-6e7f8a9b0c1d"
#     assert response.json()["name"] == "Razer Blade 14"
#     assert response.json()["description"] == "Ultra-compact gaming laptop with AMD Ryzen 9 CPU and NVIDIA RTX 4070."
#     assert response.json()["unit_price"] == 2499.00


