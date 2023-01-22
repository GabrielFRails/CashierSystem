#
# Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
#

from fastapi import APIRouter, FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI()
router = APIRouter()

class Product(BaseModel):
# {
    id_product: str = Field(
        ""
    )
    cod_product: str = Field(
        ""
    )
    description: str = Field(
        ""
    )
    unit: int = Field(
        0
    )
    price: float = Field(
        0.0
    )
    id_type: int = Field(
        0
    )
# }

class response_message(str, Enum):
	SUCCESS: str = "SUCCESS"
	FAIL: str = "FAIL"

class default_response(BaseModel):
	message: response_message

class default_response_write_operation(default_response):
	message: response_message = response_message.SUCCESS

class default_response_error(default_response):
	message: response_message = response_message.FAIL
	description: str

@app.get("/system_health")
def get_system_health():
    return {"success": True}

@app.get("/product",
    response_model=Product
)
def get_product(product_id: str):
# {
    r = Product()

    return r
# }

@app.put("/product", 
    response_model=default_response_write_operation
)
def put_product(data: Product):
# {
    return { "success": True }
# }