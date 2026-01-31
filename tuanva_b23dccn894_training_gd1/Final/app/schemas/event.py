from pydantic import BaseModel
from datetime import datetime

class EventBase(BaseModel):
    title: str
    description: str | None = None
    start_time: datetime
    end_time: datetime
    create_at: datetime
    image_url: str | None = None
    venue_id: int

class EventCreate(EventBase):
    pass
class EventUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None
    create_at: datetime | None = None
    image_url: str | None = None
    venue_id: int | None = None

class EventInDBBase(EventBase):
    id: int

    class Config:
        orm_mode = True
class Event(EventInDBBase):
    pass

class EventResponse(BaseModel):
    pass