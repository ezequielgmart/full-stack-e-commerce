import sys
import os
import pytest
from fastapi.testclient import TestClient


# 1. Obtenemos la ruta del directorio padre (la carpeta 'backend')
#    desde la ubicación de este archivo 'conftest.py'.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, "..")

# 2. Agregamos la ruta de la carpeta 'backend' al path de Python.
#    Esto garantiza que Python pueda encontrar 'main' y 'routes'.
sys.path.append(project_root)

# 3. Ahora la importación de la aplicación funcionará de forma fiable.
from main import app 

@pytest.fixture(scope="session")
def api_client() -> TestClient:
    """
    Crea un cliente de prueba para la aplicación de FastAPI,
    respetando el ciclo de vida (lifespan) para evitar warnings.
    """
    with TestClient(app) as client:
        yield client

