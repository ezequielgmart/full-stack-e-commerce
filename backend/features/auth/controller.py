from fastapi import HTTPException, status
from typing import List
from entities.auth import LoginRequest
from .service import AuthService
import bcrypt

class AuthController:

    def __init__(self, service:AuthService):
        self.service = service

    async def login(self, user_data:LoginRequest):
        result = await self.service.login(user_data.username)

        if not result:
            raise HTTPException(status_code=400, detail="Incorrect username or password")

        if not verify_password(user_data.password, result.password):
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        

        return result

def verify_password(password: str, hashed_password: str) -> bool:
    """Verifica una contraseña contra el hash almacenado."""
    # Primero, comprueba si el hash es una cadena. Si lo es, lo codifica a bytes.
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')
    
    # Ahora que sabes que es de tipo bytes, lo pasas a bcrypt
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)