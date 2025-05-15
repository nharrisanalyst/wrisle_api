from fastapi import APIRouter

table_router = APIRouter(prefix="/table", tags=['table'])

table_router.post('/')
def create_table():
    pass

table_router.get('/')
def get_table():
    pass

table_router.get('/tables')
def get_all_tables_by_user():
    pass
