from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.Repository.VenueRepository import VenueRepository
from app.schemas.venue import VenueCreate, VenueUpdate, VenueResponse

class VenueService:
    def __init__(self):
        self.repository=VenueRepository()

    def get_venue(self, db: Session, venue_id:int):
        venue=self.repository.get_by_id(db,venue_id)
        if not venue:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Venue with id {venue_id} not found"
            )
        return venue
    
    def list_venues(self, db: Session, skip: int=0, limit: int =100):
        return self.repository.get_all(db,skip,limit)
    
    def create(self,db: Session, data: VenueCreate):
        if data.capacity <=0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Capacity must be greater than zero"
            )
        return self.repository.create(db,data)
    
    def update_venue(self, db: Session, venue_id:int, data: VenueUpdate):
        venue=self.get_venue(db,venue_id)
        return self.repository.update(db,venue,data)
    
    def delete_venue(self, db: Session, venue_id:int):
        venue=self.get_venue(db,venue_id)
        self.repository.delete(db,venue)