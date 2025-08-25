from fastapi import Depends, HTTPException, status

# dependencies for the authorization token management
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timezone

from config.connect import DbPool, DB_CONFIG, TOKEN_CONFIG
from pygem.main import create_db_pool
from .repository import AuthRepository
from .service import AuthService
from .controller import AuthController
from entities.auth import TokenData # You'll need this Pydantic model for the payload

async def get_db_pool():
    pool = await create_db_pool(DB_CONFIG)
    try: 
        yield pool
    finally:
        pool.close()

async def get_auth_repository(pool:DbPool = Depends(get_db_pool)):
    return AuthRepository(pool=pool)

async def get_auth_service(
        repository: AuthRepository = Depends(get_auth_repository)
        ):
    return AuthService(repository=repository)

async def get_auth_controller(service: AuthService = Depends(get_auth_service)):
    return AuthController(service=service)        

# --- Dependencies for Token Validation ---


"""

# 1. Define the OAuth2PasswordBearer scheme
# The 'tokenUrl' should match the endpoint where you post login data.

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login"): 

This line creates the OAuth2PasswordBearer object that handles the 
logic of extracting the token from the Authorization header. 
tokenUrl="login" tells FastAPI where to redirect the user if they
try to access a protected route without a token.

"""
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

"""

get_current_user Dependency: 

This function is the core of the authentication middleware.

It uses Depends(oauth2_scheme) to automatically get the token string from the request headers.

It uses Depends(get_auth_controller) to get a fully initialized instance of your AuthController with all its dependencies.

Inside the try block, it calls jwt.decode() to verify the token's signature and expiration date.

Important: I added a check for the token's expiration date explicitly, which is a crucial part of JWT security.

It retrieves the user ID from the payload and then uses your controller (await controller.get_user_by_id(user_id)) to fetch the full user object from the database.

If any step fails, it raises an HTTPException with a 401 Unauthorized status.

algorithms as a list: I changed algorithms=TOKEN_CONFIG.get('algorithm') to algorithms=[TOKEN_CONFIG.get('algorithm')] because the jwt.decode function expects the algorithms parameter to be a list, even if it only contains one algorithm.

Explicit Expiration Check: The jwt.decode function handles the exp claim by default, but adding an explicit check like this is good practice for clarity and to catch any edge cases.

"""
# 2. Create the dependency to get the current user
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    controller: AuthController = Depends(get_auth_controller)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decode the JWT token
        payload = jwt.decode(
            token,
            TOKEN_CONFIG.get('secret_JWT_KEY'),
            algorithms=[TOKEN_CONFIG.get('algorithm')] # Note: `algorithms` must be a list
        )
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
            
    except JWTError:
        raise credentials_exception
    
    # Check if the token has expired
    # The 'exp' claim is a Unix timestamp (integer).
    # We need to compare it to the current time, also as a timestamp.
    try:
        expire_timestamp = payload.get("exp")
        if expire_timestamp is None:
            raise credentials_exception
        
        # Check for expiration
        if datetime.fromtimestamp(expire_timestamp, timezone.utc) < datetime.now(timezone.utc):
            raise credentials_exception

    except (TypeError, ValueError):
        # Handle cases where 'exp' is missing or not a valid timestamp
        raise credentials_exception

    # Use your controller to get the user from the database
    user = await controller.get_user_by_id(user_id=user_id)
    if user is None:
        raise credentials_exception
    
    return user