from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import products

app = FastAPI(title="Product QR API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router, prefix="/api/products", tags=["Products"])
