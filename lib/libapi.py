#
# Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
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