from sqlalchemy import  Column, Integer, String,DateTime,Enum,Numeric,ForeignKey

from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base
import enum

class TicketType(Base):
    __tablename__="ticket_types"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String(255),nullable=False ,primary_key=False, index=True)
    price=Column(Numeric(10,2),nullable=False, primary_key=False, index=True)
    total_quantity=Column(Integer,nullable=False, primary_key=False, index=True)
    event_id=Column(Integer,ForeignKey("events.id"),nullable=False, primary_key=False, index=True)
    events=relationship("Event", back_populates="ticket_types")
    order_items=relationship("OrderItem", back_populates="ticket_type_item")
    tickets=relationship("Ticket", back_populates="ticket_type")
