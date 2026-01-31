from sqlalchemy.orm import Session
from app.models.venue import Venue
from app.schemas.venue import VenueCreate, VenueUpdate

class VenueRepository:
    def get_by_id(self, db: Session, venue_id: int) -> Venue | None:
            return db.query(Venue).filter(Venue.id == venue_id).first()
    
    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> list[Venue]:
          return db.query(Venue).offset(skip).limit(limit).all()
    
    def create(self, db: Session, data: VenueCreate) -> Venue:
          venue=Venue(**data.model_dump())
          db.add(venue)
          db.commit()
          db.refresh(venue)
          return venue
    
    def update(self, db: Session, venue: Venue, data: VenueUpdate) -> Venue | None:
          for filed,value in data.model_dump(exclude_unset=True).items():
                setattr(venue,filed,value)
          db.commit()
          db.refresh(venue)
          return venue
    
    def delete(self, db: Session, venue: Venue) -> None:
            db.delete(venue)
            db.commit()