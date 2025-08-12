from fastapi import FastAPI
from routes.v1.products import router as product_router
from routes.v1.auth import router as auth_router
from config.connect import create_db_pool

from contextlib import asynccontextmanager

# App events in order to manage the conections pool
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating conection pool with DB")
    app.state.db_pool = await create_db_pool()
    print("Conections pool has been created succesfuly...")

    yield
    print("Closing conections pool...")

    if hasattr(app.state, 'db_pool') and app.state.db_pool:
        await app.state.db_pool.close()

app = FastAPI(
    
    title="E-commerce Api",
    description="E-commerce shop api.",
    version="0.1.0",
    lifespan=lifespan
)

# including the router
app.include_router(
    product_router,
    prefix="/products",
    tags=["Product"]
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Auth"]
)

# // start the development server
# uvicorn main:app --reload