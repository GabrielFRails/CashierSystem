#
# Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
#

from fastapi import APIRouter, FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI()
router = APIRouter()

class Product(BaseModel):
# {
    id_product: str = Field(
        "aaa99",
    )
# }

@app.get("/system_health")
def get_system_health():
    return {"success": True}

@app.get("/product",
    response_model=Product
)
def get_product(product_id: str):
# {
    r = Product(id_product=product_id)

    return r
# }