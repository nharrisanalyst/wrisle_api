from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import Base

class User(Base):
    __tablename__ = 'users'

    id:Mapped[int] = mapped_column(primary_key=True)
    email:Mapped[str] = mapped_column(nullable = False, unique=True)
    first_name:Mapped[str] = mapped_column(String(30), nullable = False)
    last_name:Mapped[str] = mapped_column(String(30), nullable = False)
    password:Mapped[str] = mapped_column(nullable= False)