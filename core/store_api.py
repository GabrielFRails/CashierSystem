#
# Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
#

from fastapi import APIRouter, FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from lib.libapi import *
from lib.libproduct import *
from lib.libetl import *

app = FastAPI()
router = APIRouter()

@app.get("/system_health")
def get_system_health():
    return {"success": True}

@app.get("/product",
    response_model=product,
    responses= {
        400: { "model": default_product_get_error }
    }
)
def get_product(product_id: str):
# {
    sql_product = product_get(product_id)
    if not sql_product:
        return JSONResponse(
		status_code=400, 
		content=default_product_get_error().dict()
	)

    p = sql_product[0]
    r = etl_product(p)

    return r
# }

@app.put("/product", 
    response_model=default_response_write_operation
)
def put_product(data: product):
# {
    return { "success": True }
# }