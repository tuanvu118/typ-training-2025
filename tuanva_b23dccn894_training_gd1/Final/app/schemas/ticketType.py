from pydantic import BaseModel
from decimal import Decimal

class TicketTypeBase(BaseModel):
    name:str
    price:float
    total_quantity:int
    event_id:int

class TicketTypeCreate(TicketTypeBase):
    pass

class TicketTypeUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    total_quantity: int | None = None
    event_id: int | None = None

class TicketTypeInDBBase(TicketTypeBase):
    id:int

    class Config:
        orm_mode = True
class TicketType(TicketTypeInDBBase):
    pass

class TicketTypeResponse(BaseModel):
    pass