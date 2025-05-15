import uuid
import datetime
from fastapi_users import schemas

class UserRead(schemas.BaseUser[uuid.UUID]):
    id:uuid.UUID
    email:str
    first_name:str
    last_name:str
    birthday:datetime.date

class UserCreate(schemas.BaseUserCreate):
    first_name:str
    last_name:str
    birthday:datetime.date

class UserUpdate(schemas.BaseUserUpdate):
    first_name:str
    last_name:str
    birthday:datetime.date