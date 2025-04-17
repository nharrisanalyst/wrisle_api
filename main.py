import uuid

from fastapi import FastAPI
from fastapi_users import FastAPIUsers
import sqlalchemy
from .routes import login
from models.main_db import User
from auth.UserManager import get_user_manager
from auth.Auth_Backend import auth_backend
from .schemas import UserCreate, UserRead

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)


app =  FastAPI()

# Include routers
app.include_router(login.router)

@app.get("/")
async def read_root():
    return {"endpoint":"Wrisle"}


@app.get("/hello")
async def read_hello():
    return {"hello":"world"}

@app.get("/alchemy")
async def read_alchemy_version():
    return{'alchemy-version':sqlalchemy.__version__}


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)