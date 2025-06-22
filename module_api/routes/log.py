from fastapi import APIRouter, HTTPException, Request, Depends
from module_api.auth import verify_basic_auth, verify_bearer_auth

router = APIRouter()

@router.post("/log")
async def submit_json(data: dict, request: Request):
    connection = None
    cursor = None
    addLog(request.client.host, data)

@router.get("/info")
async def submit_json(data: dict, request: Request):
    connection = None
    cursor = None
    print("HellYeah")