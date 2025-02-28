from fastapi import APIRouter

router = APIRouter()

products = [
    {"id": 1, "name": "Smartphone", "price": 25999},
    {"id": 2, "name": "Wireless Headphones", "price": 3499},
    {"id": 3, "name": "Smartwatch", "price": 4999},
]

@router.get("/products")
def get_products():
    return {"products": products}

