from fastapi import APIRouter, HTTPException, Request, Depends
from module_api.auth import verify_basic_auth, verify_bearer_auth
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST

router = APIRouter()

@router.get("/metrics")
def metrics():

    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}
