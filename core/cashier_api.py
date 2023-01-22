#
# Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
#

from fastapi import APIRouter, FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum

from lib.libapi import *

app = FastAPI()
router = APIRouter()

@app.get("/system_health")
def get_system_health():
    return {"success": True}

@app.get("/product",
    response_model=product
)
def get_product(product_id: str):
# {
    r = product()

    return r
# }

@app.put("/product", 
    response_model=default_response_write_operation
)
def put_product(data: product):
# {
    return { "success": True }
# }