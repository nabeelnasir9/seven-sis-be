from fastapi import APIRouter, HTTPException
from app.core.database import product_collection
from app.schemas.product import ProductResponse

router = APIRouter()

@router.get("/{equipment_id}", response_model=ProductResponse)
async def get_product(equipment_id: str):
    product = product_collection.find_one({"equipment_id": equipment_id}, {'_id': False})

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product
