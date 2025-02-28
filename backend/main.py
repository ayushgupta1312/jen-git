from fastapi import FastAPI
from routes.products import router as product_router

app = FastAPI()

app.include_router(product_router)

@app.get("/")
def home():
    return {"message": "Welcome to MyShop API"}

# Run this API with: uvicorn main:app --reload
 
