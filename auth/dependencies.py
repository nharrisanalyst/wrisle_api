import uuid
from ..auth.UserManager import get_user_manager
from ..models.main_db import User
from ..auth.Auth_Backend import auth_backend
from fastapi_users import FastAPIUsers


fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

current_active_user = fastapi_users.current_user(active=True)