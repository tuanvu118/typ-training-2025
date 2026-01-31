from pydantic import BaseModel

class TicketBase(BaseModel):
    event_id:int
    ticket_tupe_id:int
    user_id:int
    order_id:int
    status:str

class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    pass

class TicketInDBBase(TicketBase):
    id:int

    class Config:
        orm_mode = True
class Ticket(TicketInDBBase):
    pass