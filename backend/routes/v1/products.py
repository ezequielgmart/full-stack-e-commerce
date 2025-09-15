from fastapi import APIRouter, Depends, Query
from typing import List
from entities.product import Product, ProductApiResponse, ProductAllDetails, ProductAllDetailsWithImages
from features.products.dependencies import get_product_controller
from features.products.controller import ProductController

router = APIRouter()

# 1. Ruta sin parámetros
@router.get("/",
    response_model=ProductApiResponse,
    summary="Obtener todos los products con un limit o los que el nombre coincida",
    description="Retorna una lista de todos los productos disponibles en el sistema limitados para paginacion, o tambien puede recibir un termino de busqueda."
)
async def get_products(
    search: str = Query(None),
    sort_by: str = Query(None),
    order: str = Query(None),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    controller: ProductController = Depends(get_product_controller)
):
    if search == None:
        return await controller.get_all(limit=limit, offset=offset, sort_by=sort_by, order=order)
    else: 
        return await controller.get_all_products_by_name_like(
            key_value=search,
            limit=limit, 
            offset=offset,
            sort_by=sort_by,
            order = order
        )

# 3. La ruta dinámica más genérica debe ir al final
@router.get("/{product_id}",
    response_model=ProductAllDetailsWithImages,
    summary="Obtener un product by id",
    description="Retorna una un solo Product Model"
)
async def get_product_by_id(
    product_id: str,
    controller: ProductController = Depends(get_product_controller)
):
    return await controller.get_product_by_id_all_details(
        product_id=product_id
    )