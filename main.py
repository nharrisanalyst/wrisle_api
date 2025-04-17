import uuid

from fastapi import FastAPI
from fastapi_users import FastAPIUsers
import sqlalchemy
from .routes import login
from models.main_db import User
from auth.UserManager import get_user_manager

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

