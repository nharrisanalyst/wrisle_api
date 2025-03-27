from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

router = APIRouter(prefix="/login", tags=['login'])

## sample secretkey 
SECRET_KEY = "5c28bd35fcaa4ca45b9e967707b2883e18d563c0e66b7c2b7a8301e1c9b428bc"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

@router.post('/')
def login_route():
    return {'route':'login'}