from sqlalchemy.orm import Session
from fastapi import UploadFile
from app.Repository.EventRepository import EventRepository
from app.schemas.event import EventCreate, EventUpdate, Event
from app.Service.cloudinaryService import upload_image, delete_image

repo=EventRepository()

class EventService:
    def create_event(self, db: Session, data: EventCreate, image: UploadFile | None) -> Event:
        if image:
            url,public_id = upload_image(image)
            data_dict=data.model_dump()
            data_dict["image_url"]=url
        event = EventCreate(**data_dict)
        return repo.create(db, event)
    
    def get_event(self, db: Session, event_id:int) -> Event | None:
        return repo.get_by_id(db, event_id)
    
    