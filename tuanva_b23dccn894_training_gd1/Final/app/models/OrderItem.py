from sqlalchemy import  Column, Integer, String,DateTime,Enum,ForeignKey,Numeric

from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base
import enum


class OrderItem(Base):
    __tablename__="order_items"
    id=Column(Integer, primary_key=True, index=False)
    order_id=Column(Integer,ForeignKey("order.id"),nullable=False, primary_key=False, index=True)
    ticket_type_item_id=Column(Integer,ForeignKey("ticket_types.id"),nullable=False, primary_key=False, index=True)
    quantity=Column(Integer,nullable=False, primary_key=False, index=True)
    order=relationship("Order", back_populates="order_items")
    ticket_type_item=relationship("TicketType", back_populates="order_items")



    