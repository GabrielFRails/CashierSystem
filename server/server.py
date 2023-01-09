from fastapi import APIRouter, FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
router = APIRouter()

@app.get("/system_health")
def get_system_health():
    return {"success": True}