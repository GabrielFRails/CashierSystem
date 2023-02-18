#
# Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
# Copyright (c) 2023 Luiza Costa <oliveiraluiza2012ufg@gmail.com>
#

from fastapi import APIRouter, FastAPI, Query
from fastapi.responses import JSONResponse
from typing import Union

from lib.libapi import *
from lib.libproduct import *
from lib.libproducttype import *
from lib.libetl import *
from lib.libcustomer import *

app = FastAPI()
router = APIRouter()

#product's routes
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
		content=default_list_get_error().dict()
	)

    product_list.sort(key=lambda x: x.id_product)
    response = {
        "products": product_list,
        "count": len(product_list)
    }

    return response
# }

@app.put("/product", 
    response_model=Union[default_response_write_operation, dict],
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

@app.post("/product", 
    response_model=default_response_write_operation,
    summary="Create product data"
)
def post_product(data: product_request):
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

#product type's routes
@app.get("/product/type",
    response_model = product_type,
    responses = {
        400: { "model": default_product_type_get_error }
    }
)
def get_product_type(product_type_id: str= Query(
    title = "",
    description = "Product Type id"
)):
    sql_product_type = product_type_get(product_type_id)
    if sql_product_type == -1:
        return JSONResponse(
            status_code = 400,
            content = default_product_type_get_error().dict()
        )
    
    p = sql_product_type[0]
    r = etl_product_type(p)

    return r

@app.get("/product/type/list",
    response_model = product_type_list,
    responses = {
        400: { "model": default_product_type_get_error }
    }
)
def get_product_type_list():
    product_type_list = product_type_all_get()
    if not len(product_type_list) > 0:
        return JSONResponse(
            status_code = 400,
            content = default_product_type_list_get_error().dict()
        )
    
    product_type_list.sort(key=lambda x: x.id_type)
    response = {
        "product_types": product_type_list,
        "count": len(product_type_list)
    }

    return response

@app.put("/product/type",
    response_model = default_response_write_operation,
    summary = "Update product type"
)
def put_product_type(data: product_type):
    r = product_type_update(data)

    if r == -1:
        return JSONResponse(
            status_code = 400,
            content = default_response_writefail_operation().dict()
        )

    response = default_response_write_operation().__dict__
    return response

@app.post("/product/type",
    response_model = default_response_write_operation,
    summary = "Create product type data"
)
def put_product_type(data: product_type_request):
    r = product_type_post(data)

    if r == -1:
        return JSONResponse(
            status_code = 400,
            content = default_response_writefail_operation().dict()
        )

    response = default_response_write_operation().__dict__
    return response

@app.delete("/product/type",
    response_model = Union[default_response_write_operation, dict],
    summary = "Delete product type data"
)
def delete_product_type(product_type_id: str = Query(
    title = "",
    description = "Product type id"
)):
    rows_deleted = product_type_delete(product_type_id)

    if not rows_deleted:
        return {
            "message": "FAIL",
            "description": "0 rows deleted"
        }

    response = default_response_write_operation().__dict__
    return response

#customer's routes
@app.get("/customer",
    response_model=customer,
    responses= {
        400: { "model": default_product_get_error }
    }
)
def get_customer(customer_id: str = Query(
    title="",
    description="Customer id"
)):
# {
    sql_product = customer_get(customer_id)
    if sql_product == -1:
        return JSONResponse(
		status_code=400, 
		content=default_product_get_error().dict()
	)

    c = sql_product[0]
    r = etl_customer(c)

    return r
# }

@app.get("/customer/list",
    response_model=customer_list,
    responses= {
        400: { "model": default_product_get_error }
    }
)
def get_customer_list():
# {
    customer_list = customer_all_get()
    if not len(customer_list) > 0:
        return JSONResponse(
		status_code=400, 
		content=default_list_get_error().dict()
	)

    customer_list.sort(key=lambda x: x.id_customer)
    response = {
        "customers": customer_list,
        "count": len(customer_list)
    }

    return response
# }

@app.put("/customer", 
    response_model=Union[default_response_write_operation, dict],
    summary="Update customer data"
)
def put_customer(data: customer):
# {
    r = customer_update(data)

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

@app.post("/customer", 
    response_model=default_response_write_operation,
    summary="Create customer data"
)
def post_customer(data: customer_request):
# {
    r = customer_post(data)

    if r == -1:
        return JSONResponse(
		status_code=400, 
		content=default_response_writefail_operation().dict()
	)

    response = default_response_write_operation().__dict__
    return response
# }

@app.delete("/customer",
    response_model=Union[default_response_write_operation, dict],
    summary="Delete customer data"
)
def delete_product(customer_id: str = Query(
    title="",
    description="Customer id"
)):
# {
    rows_deleted = customer_delete(customer_id)

    if not rows_deleted:
        return {
            "success": False,
            "message": "0 rows deleted"
        }

    response = default_response_write_operation().__dict__
    return response
# }