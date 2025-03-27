from fastapi import FastAPI
import sqlalchemy
from .routes import login


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

