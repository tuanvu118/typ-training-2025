from sqlalchemy import  Column, Integer, String,DateTime,Enum,ForeignKey,Numeric

from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base
import enum

class TicketStatus(enum.Enum):
    HOLD="hold"
    CONFIRMED="confirmed"
    EXPIRED="expired"
    CANCELED="canceled"
    
class Ticket(Base):
    __tablename__="ticket"
    id=Column(Integer, primary_key=True, index=True)
    event_id=Column(Integer,ForeignKey("events.id"),nullable=False, primary_key=False, index=True)
    ticket_type_id=Column(Integer,ForeignKey("ticket_types.id"),nullable=False, primary_key=False, index=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False, primary_key=False, index=True)
    order_id=Column(Integer,ForeignKey("order.id"),nullable=False, primary_key=False, index=True)
    status=Column(Enum(TicketStatus,name='ticket_status'),nullable=False, default=TicketStatus.HOLD)
    create_at=Column(DateTime,default=datetime.utcnow,primary_key=False, index=True)
    event=relationship("Event", back_populates="tickets")
    ticket_type=relationship("TicketType", back_populates="tickets")
    user=relationship("User", back_populates="tickets")
    order=relationship("Order", back_populates="tickets")