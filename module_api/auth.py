from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials, HTTPBearer, HTTPAuthorizationCredentials

security_basic = HTTPBasic()
security_bearer = HTTPBearer()

def verify_basic_auth(credentials: HTTPBasicCredentials = Depends(security_basic)):
    correct_username = "admin"
    correct_password = "secret"
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid basic auth")
    return credentials.username

def verify_bearer_auth(credentials: HTTPAuthorizationCredentials = Depends(security_bearer)):
    if credentials.scheme.lower() != "bearer" or credentials.credentials != "secrettoken123":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid bearer token")
    return credentials.credentials