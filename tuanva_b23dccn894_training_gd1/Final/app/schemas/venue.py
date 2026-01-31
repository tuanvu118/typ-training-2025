from pydantic import BaseModel

class VenueBase(BaseModel):
    name: str
    address: str
    capacity: int

class VenueCreate(VenueBase):
    pass
class VenueUpdate(BaseModel):
    name: str | None = None
    address: str | None = None
    capacity: int | None = None

class VenueInDBBase(VenueBase):
    id: int

    class Config:
        orm_mode = True
class VenueResponse(VenueInDBBase):
    pass