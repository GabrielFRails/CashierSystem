#
# Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
#

from fastapi import APIRouter, FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import Union

from lib.libapi import *
from lib.libproduct import *
from lib.libproducttype import *
from lib.libetl import *
from lib.libcart import *

app = FastAPI()
router = APIRouter()

@app.get("/cart",
    response_model=cart,
    responses= {
        400: { "model": default_product_get_error }
    }
)
def get_cart(cart_id: str = Query(
    title="",
    description="cart id"
)):
# {
    sql_product = cart_get(cart_id)
    if sql_product == -1:
        return JSONResponse(
		status_code=400, 
		content=default_product_get_error().dict()
	)

    c = sql_product[0]
    r = etl_cart(c)

    return r
# }

@app.get("/cart/list",
    response_model=cart_list,
    responses= {
        400: { "model": default_product_get_error }
    }
)
def get_cart_list():
# {
    cart_list = cart_all_get()
    if not len(cart_list) > 0:
        return JSONResponse(
		status_code=400, 
		content=default_list_get_error().dict()
	)

    cart_list.sort(key=lambda x: x.id_cart)
    response = {
        "carts": cart_list,
        "count": len(cart_list)
    }

    return response
# }

@app.put("/cart", 
    response_model=Union[default_response_write_operation, dict],
    summary="Update cart data"
)
def put_cart(data: cart):
# {
    r = cart_update(data)

    if r == -1:
        return JSONResponse(
		status_code=400, 
		content=default_response_writefail_operation().dict()
	)

    if r == 0:
        return JSONResponse(
		status_code=400, 
		content={
            "success": "FALSE",
            "message": "id not found"
        }
	)

    response = default_response_write_operation().__dict__
    return response
# }

@app.post("/cart", 
    response_model=default_response_write_operation,
    summary="Create cart data"
)
def post_cart(data: cart_request):
# {
    r = cart_post(data)

    if r == -1:
        return JSONResponse(
		status_code=400, 
		content=default_response_writefail_operation().dict()
	)

    response = default_response_write_operation().__dict__
    return response
# }

@app.delete("/cart",
    response_model=Union[default_response_write_operation, dict],
    summary="Delete cart data"
)
def delete_product(cart_id: str = Query(
    title="",
    description="cart id"
)):
# {
    rows_deleted = cart_delete(cart_id)

    if not rows_deleted:
        return {
            "success": False,
            "message": "0 rows deleted"
        }

    response = default_response_write_operation().__dict__
    return response
# }