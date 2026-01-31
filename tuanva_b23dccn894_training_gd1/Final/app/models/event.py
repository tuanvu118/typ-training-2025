from sqlalchemy import  Column, Integer, String,DateTime,Enum,ForeignKey

from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base


import enum

class Event(Base):
    __tablename__="events"
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String(255),nullable=False ,primary_key=False, index=True)
    description=Column(String(255),nullable=True, primary_key=False, index=True)
    start_time=Column(DateTime(timezone=True),nullable=False, primary_key=False, index=True)
    end_time=Column(DateTime(timezone=True),nullable=False, primary_key=False, index=True)
    create_at=Column(DateTime,default=datetime.utcnow,primary_key=False, index=True)
    venue_id=Column(Integer,ForeignKey("venues.id"),nullable=False, primary_key=False, index=True)
    image_url=Column(String(255),nullable=True ,primary_key=False, index=True)
    venue=relationship("Venue", back_populates="events")
    ticket_types=relationship("TicketType", back_populates="events")
    tickets=relationship("Ticket", back_populates="event")


    