import uuid
from typing import TYPE_CHECKING
from sqlalchemy import String, Date
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from .dependencies import Base

if TYPE_CHECKING:
    from .main_db import User

class DataTable(Base):
    __tablename__ ='data_table'

    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(500))
    
    userId:Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id" , ondelete="CASCADE"))
    user:Mapped['User'] = relationship("DataTable",back_populates = 'data_tables')

    bucket:Mapped[str] = mapped_column(String(20))
    filename:Mapped[str] = mapped_column(String(250))

    def get_s3_key(self)->str:
        return f"user-data/{self.id}/{self.filename}"