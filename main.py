from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlalchemy
from .auth.Auth_Backend import auth_backend
from .schemas.UserSchemas import UserCreate, UserRead, UserUpdate
from .settings import settings
from .routes.table import table_router
from .auth.dependencies import fastapi_users

origins = [
    "http://localhost:6006",
    "http://localhost:5173"
]



app =  FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
#app.include_router(login.router)

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

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

app.include_router(
    table_router
    )