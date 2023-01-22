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