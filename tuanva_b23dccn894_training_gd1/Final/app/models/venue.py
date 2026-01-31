from sqlalchemy import  Column, Integer, String,DateTime,Enum

from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base
import enum

class Venue(Base):
    __tablename__="venues"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String(255),nullable=False ,primary_key=False, index=True)
    address=Column(String(255),nullable=False, primary_key=False, index=True)
    capacity=Column(Integer,nullable=False, primary_key=False, index=True)
    events=relationship("Event", back_populates="venue")
