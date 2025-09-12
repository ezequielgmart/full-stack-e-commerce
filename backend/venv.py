""" 
this script automaticly launch a new terminal starting de virtual enviroment and the product server 

Este archivo es un script the python que automaticamente lanza una nueva terminal e inicia el servidor
"""
import subprocess
import os 

# settings

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(SCRIPT_DIR, "scripts","venv.bat")


def start_venv():
    """Launch the terminal for a frontend server"""
    print(f"running frontend script... {SCRIPT_PATH}")
    subprocess.run(f'start cmd /k "{SCRIPT_PATH}"', shell=True)

def main():
    try:
        print("Launching Venv...")
        start_venv()
    
    except FileNotFoundError:
        print("Error: No se pudo encontrar el emulador de terminal.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__": 

    main()
    print("✅ Venv completed!")