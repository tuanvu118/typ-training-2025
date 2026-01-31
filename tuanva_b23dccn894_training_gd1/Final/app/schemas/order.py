from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime
from typing import List

class OrderBase(BaseModel):
    user_id:int
    total_amount: Decimal
    status: str | None = "pending"

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    pass

class OrderInDBBase(OrderBase):
    id: int
    create_at: datetime
    pass

    class Config:
        orm_mode=True
class Order(OrderInDBBase):
    pass

class HoldItem(BaseModel):
    ticket_type_id:int
    quantity:int

class OrderHoldRequest(BaseModel):
    items: List[HoldItem]

class OrderConfirmRequest(BaseModel):
    session_id: str
    hold_token: str

