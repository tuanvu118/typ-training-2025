from sqlalchemy import  Column, Integer, String,DateTime,Enum

from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base
import enum

class UserRole(enum.Enum):
    ADMIN="admin"
    USER="user"

class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, index=True)
    email=Column(String(255),nullable=False ,primary_key=False, index=True)
    password=Column(String(255),nullable=False, primary_key=False, index=True)
    full_name=Column(String(255),nullable=False,primary_key=False, index=True)
    role=Column(Enum(UserRole,name='user_role'),nullable=False, default=UserRole.USER)
    create_at=Column(DateTime,default=datetime.utcnow,primary_key=False, index=True)
    orders=relationship("Order", back_populates="user")
    tickets=relationship("Ticket", back_populates="user")