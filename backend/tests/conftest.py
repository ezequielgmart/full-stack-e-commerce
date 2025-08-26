# # conftest.py

import sys
import os
import pytest
# from httpx import AsyncClient # <-- Import AsyncClient from httpx
# from fastapi.testclient import TestClient # Keep this one if you need it for other tests

# # Obtén la ruta del proyecto
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, "..")
sys.path.append(project_root)

# # Importa la aplicación
# from backend.main import app 

# @pytest.fixture
# async def api_client():
#     # Use the AsyncClient with the 'app' argument
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         yield ac