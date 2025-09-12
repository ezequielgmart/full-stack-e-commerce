""" 
this script automaticly launch a new terminal starting de virtual enviroment and the product server 

Este archivo es un script the python que automaticamente lanza una nueva terminal e inicia el servidor
"""
import subprocess
import os 

# settings

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SERVER_SCRIPT_PATH = os.path.join(SCRIPT_DIR, "scripts","server.bat")
FRONTEND_SCRIPT_PATH = os.path.join(SCRIPT_DIR, "scripts","frontend.bat")

def start_backend_server():
    print(f"running script: {SERVER_SCRIPT_PATH}")
    subprocess.run(f'start cmd /k "{SERVER_SCRIPT_PATH}"', shell=True)

def start_frontend_server():
    """Launch the terminal for a frontend server"""
    print(f"running frontend script... {FRONTEND_SCRIPT_PATH}")
    subprocess.run(f'start cmd /k "{FRONTEND_SCRIPT_PATH}"', shell=True)

def main():
    try:
        print("Launching Backend server...")
        start_backend_server()
        
        print("Launching Frontend Dev Server...")
        start_frontend_server()
    except FileNotFoundError:
        print("Error: No se pudo encontrar el emulador de terminal.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__": 
    
    print("🚀 Starting full-stack dev enviroment...")
    main()
    print("✅ Launch completed!")