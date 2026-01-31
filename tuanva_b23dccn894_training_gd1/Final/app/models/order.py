from sqlalchemy import  Column, Integer, String,DateTime,Enum,ForeignKey,Numeric

from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base
import enum

class OrderStatus(enum.Enum):
    PENDING="pending"
    COMPLETED="completed"
    CANCELED="canceled"
    EXPIRED="expired"

class Order(Base):
    __tablename__="order"
    id=Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False, primary_key=False, index=True)
    total_amount=Column(Numeric(10,2),nullable=False, primary_key=False, index=True) 
    status=Column(Enum(OrderStatus,name='order_status'),nullable=False, default=OrderStatus.PENDING)
    create_at=Column(DateTime,default=datetime.utcnow,primary_key=False, index=True)
    user=relationship("User", back_populates="orders")
    order_items=relationship("OrderItem", back_populates="order")
    tickets=relationship("Ticket", back_populates="order")




    