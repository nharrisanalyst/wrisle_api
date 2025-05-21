from collections.abc import AsyncGenerator
from typing import TYPE_CHECKING
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from datetime import date
from typing import List
from sqlalchemy import String, Date
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from .dependencies import Base


if TYPE_CHECKING:
    from .table_db import DataTable


DATABASE_URL ="postgresql+asyncpg://nathanharris:Scout:1185@localhost:5432/wrisle_db"


class User(SQLAlchemyBaseUserTableUUID, Base):
    first_name:Mapped[str] = mapped_column(String(30))
    last_name:Mapped[str] = mapped_column(String(30))
    birthday:Mapped[date] = mapped_column(Date)
    tables: Mapped[List["DataTable"]] = relationship("DataTable", back_populates="user")


engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)