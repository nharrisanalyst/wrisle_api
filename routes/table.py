from fastapi import APIRouter, Depends
from ..auth.dependencies import current_active_user
from ..models.main_db import User

table_router = APIRouter(prefix="/table", tags=['table'])

@table_router.post('/')
def make_table(user: User = Depends(current_active_user)):
    pass

@table_router.get('/table-upload-url')
def get_table_uplaod_url(user: User = Depends(current_active_user)):

    return {"first_name":user.first_name}

@table_router.get('/table-download-url')
def get_table_download_url():
    pass


