#
# Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
# Copyright (c) 2023 Luiza Costa <oliveiraluiza2012ufg@gmail.com>
#

from pydantic import BaseModel
from enum import Enum
from pydantic import BaseModel, Field

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

class default_product_get_error(default_response_error):
    description: str = "Product not found"

class default_list_get_error(default_response_error):
    description: str = "No product data found in database"

class default_product_type_get_error(default_response_error):
    description: str = "Product type not found"    

class default_product_type_list_get_error(default_response_error):
    description: str = "No product type data found in database"

class default_response_writefail_operation(default_response_error):
	description: str = "Fail to insert data in database"

class product(BaseModel):
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

class product_request(BaseModel):
# {
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

class product_list(BaseModel):
# {
    products: list[product] = Field(
        []
    )
    count: int = Field(
        0
    )
# }

class product_type(BaseModel):
    id_type: str = Field(
        ""
    )
    description: str = Field(
        ""
    )

class product_type_request(BaseModel):
    description: str = Field(
        ""
    )

class product_type_list(BaseModel):
    product_types: list[product_type] = Field(
        []
    )
    count: int = Field(
        0
    )

class customer(BaseModel):
    id_customer: int = Field(
        0   
    )
    name: str = Field(
        ""
    )
    phone: str = Field(
        ""
    )

class customer_list(BaseModel):
# {
    customers: list[customer] = Field(
        []
    )
    count: int = Field(
        0
    )
# }

class customer_request(BaseModel):
    name: str = Field(
        ""
    )
    phone: str = Field(
        ""
    )

class cart(BaseModel):
    id_cart: int = Field(
        0   
    )
    sum: float = Field(
        0.0
    )
    discount: float = Field(
        0.0
    )
    final_price: float = Field(
        0.0
    )
    id_customer: int = Field(
        0   
    )
    cart_status: str = Field(
        ""
    )

class cart_list(BaseModel):
# {
    carts: list[cart] = Field(
        []
    )
    count: int = Field(
        0
    )
# }

class cart_request(BaseModel):
    id_customer: int = Field(
        0   
    )

class cart_products(BaseModel):
    id_cart: int = Field(
        None   
    )
    id_product: int = Field(
        None   
    )
    quantity: int = Field(
        1   
    )

class final_cart(BaseModel):
    id_cart: int = Field(
        None   
    )
    discount: float = Field(
        None
    )