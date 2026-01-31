from sqlalchemy.orm import Session
from app.models.event import Event
from app.schemas.event import EventCreate, EventUpdate

class EventRepository:
    def create(self, db: Session, data: EventCreate) -> Event:
        event=Event(**data.dict())
        db.add(event)
        db.commit()
        db.refresh(event)
        return event
    
    def get_by_id(self, db: Session, event_id: int) -> Event | None:
        return db.query(Event).filter(Event.id == event_id).first()
    
    