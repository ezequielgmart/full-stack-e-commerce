import sys
import os
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient


# 1. Obtenemos la ruta del directorio padre (la carpeta 'backend')
#    desde la ubicación de este archivo 'conftest.py'.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, "..")

# 2. Agregamos la ruta de la carpeta 'backend' al path de Python.
#    Esto garantiza que Python pueda encontrar 'main' y 'routes'.
sys.path.append(project_root)

# 3. Ahora la importación de la aplicación funcionará de forma fiable.
from backend.main import app 

@pytest.fixture
async def api_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

