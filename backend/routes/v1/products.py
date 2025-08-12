from fastapi import APIRouter, Depends, Query
from typing import List
from entities.product import Product
from features.products.dependencies import get_product_controller
from features.products.controller import ProductController

router = APIRouter()


"""
# TODO
* Debo de hacerle una paginacion (ready)
* Por categoria

"""
@router.get(
    "/",
    response_model=List[Product],
    summary="Obtener todos los products",
    description="Retorna una lista de todos los productos disponibles en el sistema."
    
)
async def get_products(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    controller: ProductController = Depends(get_product_controller)
    ):
    return await controller.get_all(limit = limit, offset = offset)

# get product by id
@router.get(
    "/{product_id}",
    response_model=Product,
    summary="Obtener un product by id",
    description="Retorna una un solo Product Model"
    
)
async def get_products(
    product_id: str,
    controller: ProductController = Depends(get_product_controller)
    ):
    return await controller.get_by_id(
        product_id=product_id
    )

# get all the products by category
# all/ => added para diferenciar el product_id de el general por categoria.  
@router.get(
    "/all/{category_id}",
    response_model=List[Product],
    summary="Obtener todos los products",
    description="Retorna una lista de todos los productos disponibles en el sistema."
    
)
async def get_products(
    category_id: str,
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    controller: ProductController = Depends(get_product_controller)
    ):
    return await controller.get_all_products_by_category(
        filter_key_value=category_id,
        limit = limit, 
        offset = offset
    )

# this is for the search
@router.get(
    "/search/{product_name}",
    response_model=List[Product],
    summary="Obtener los product que el nombre coincida",
    description="Retorna una lista de productos"
    
)
async def search_products_by_name(
    product_name: str,
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    controller: ProductController = Depends(get_product_controller)
    ):
    return await controller.get_all_products_by_name_like(
        key_value=product_name,
        limit = limit, 
        offset = offset
    )