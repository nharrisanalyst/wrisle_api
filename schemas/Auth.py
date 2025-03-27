from pydantic import BaseModel

class LoginRequest(BaseModel):
    username:str
    password:str

class AuthResponse(BaseModel):
    token:str