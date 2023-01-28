#
# Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
#

from fastapi import APIRouter, FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import Union

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
def get_product(product_id: str = Query(
    title="",
    description="Product id"
)):
# {
    sql_product = product_get(product_id)
    if sql_product == -1:
        return JSONResponse(
		status_code=400, 
		content=default_product_get_error().dict()
	)

    p = sql_product[0]
    r = etl_product(p)

    return r
# }

@app.get("/product/list",
    response_model=product_list,
    responses= {
        400: { "model": default_product_get_error }
    }
)
def get_product_list():
# {
    product_list = product_all_get()
    if not len(product_list) > 0:
        return JSONResponse(
		status_code=400, 
		content=default_productlist_get_error().dict()
	)

    response = {
        "products": product_list,
        "count": len(product_list)
    }

    return response
# }

@app.put("/product", 
    response_model=default_response_write_operation,
    summary="Update product data"
)
def put_product(data: product):
# {
    r = product_update(data)

    if r == -1:
        return JSONResponse(
		status_code=400, 
		content=default_response_writefail_operation().dict()
	)

    response = default_response_write_operation().__dict__
    return response
# }

@app.post("/product", 
    response_model=default_response_write_operation,
    summary="Create product data"
)
def put_product(data: product_request):
# {
    r = product_post(data)

    if r == -1:
        return JSONResponse(
		status_code=400, 
		content=default_response_writefail_operation().dict()
	)

    response = default_response_write_operation().__dict__
    return response
# }

@app.delete("/product",
    response_model=Union[default_response_write_operation, dict],
    summary="Delete product data"
)
def delete_product(product_id: str = Query(
    title="",
    description="Product id"
)):
# {
    rows_deleted = product_delete(product_id)

    if not rows_deleted:
        return {
            "success": False,
            "message": "0 rows deleted"
        }

    response = default_response_write_operation().__dict__
    return response
# }
