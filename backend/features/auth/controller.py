from fastapi import HTTPException, status
from typing import Optional
from entities.auth import LoginRequest, TokenData, RegisterRequest, NewUserResponse
from entities.users import User, UserPublic
from config.connect import TOKEN_CONFIG
from .service import AuthService
import uuid

# jwt validation
import bcrypt
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta,  timezone
from fastapi import HTTPException, status


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthController:

    def __init__(self, service:AuthService):
        self.service = service

    async def login(self, user_data:LoginRequest):

        result = await self.service.login(user_data.username)

        if not result:
            raise HTTPException(status_code=400, detail="Incorrect username or password")

        if not self.verify_password(user_data.password, result.password):
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        
        # anterior mente me retornaba la info del usuario logeado. Entonces ahora lo que debe de hacer es retornarme el token creado. 

        # return result

        ## 8/12 - Este codigo es para devolver el token creado si se loguea satisfactoria mente

        # Corrected line: Convert the UUID to a string
        access_token_payload = {"sub": str(result.user_id)}

        try:
            expire_in_minutes = int(TOKEN_CONFIG['access_token_expire_minutes'])
        except (ValueError, TypeError):
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Token expiration time is not configured correctly."
            )
        
        expires_delta = timedelta(minutes=expire_in_minutes)

        access_token = self.create_access_token(
            data=access_token_payload,
            expires_delta=expires_delta
        )

        # FastAPI recomienda un formato específico para los tokens de portador (bearer tokens)
        return {"access_token": access_token, "token_type": "bearer"}

    """ ESTO FUE MOVIDO A USERS """
    # async def register(self, data:RegisterRequest) -> User:
        
    #     # hay que hashear la contraseña antes de pasar al servicio
    #     hashed_password = self.get_password_hash(data.password)

    #     data_for_service = {
    #         "user_id":str(uuid.uuid4()),
    #         "email":data.email,
    #         "username":data.username,   
    #         "password":str(hashed_password)
    #     }

    #     new_user = NewUserResponse(**data_for_service)

    #     return await self.service.register(new_user)


    # Hashing y verificación de contraseñas
    def get_password_hash(self, password: str):
        return pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str):
        # Primero, comprueba si el hash es una cadena. Si lo es, lo codifica a bytes.
        if isinstance(hashed_password, str):
            hashed_password = hashed_password.encode('utf-8')

        return pwd_context.verify(plain_password, hashed_password)

    
    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None): 
        # Copia los datos para no modificar el diccionario original
        to_encode = data.copy()

        # Calcula la fecha de expiración
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        
        else:

            try:

                expire_minutes = int(TOKEN_CONFIG.get('access_token_expire_minutes', 30))

            except (ValueError, TypeError):
                to_encode.update({"exp": expire})

            expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)

        # Actualiza el payload con la fecha de expiración
        to_encode.update({"exp": expire})
        
        # codifica el JWT
        encoded_jwt = jwt.encode(
            to_encode, 
            TOKEN_CONFIG['secret_JWT_KEY'], 
            algorithm=TOKEN_CONFIG['algorithm']
        )

        return encoded_jwt
    
    async def get_current_user(self, token:str):

        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access denied",
            headers={"WWW-Authenticate": "Bearer"},
        )

        try:

            payload = jwt.decode(token, TOKEN_CONFIG['secret_JWT_KEY'], algorithms=TOKEN_CONFIG['algorithm'])
            user_id: str = payload.get("sub")
            if user_id is None:
                raise credentials_exception
            token_data = TokenData(user_id=user_id)

        except JWTError:
            raise credentials_exception
        
        user = await self.service.get_user_by_id(user_id=token_data.user_id)
        if user is None:
            raise credentials_exception
        return user

    def generate_user_id(self, username:str) -> uuid.UUID:
        new_uuid = uuid.uuid4(username)
        return new_uuid
    
    async def get_public_user(self, user_id:str) -> UserPublic:
        # aqui deberia de estar la verificacion del token.
        #  
        user = await self.service.get_public_user(user_id)  

        if not user:
            # Raise an HTTPException with a 404 status code
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User not found"
            )
        
        return user   
    
    async def get_user_by_id(self, user_id:str)-> UserPublic:
        return await self.service.get_user_by_id(user_id)