from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Form, status
from sqlalchemy.orm import Session
from datetime import datetime

from app.schemas.event import EventCreate, EventUpdate, Event, EventResponse
from app.Service.EventService import EventService
from app.api.deps import get_db, require_admin

router = APIRouter()

@router.post("/",response_model=EventCreate, status_code=status.HTTP_201_CREATED)
def create_event(
    title: str=Form(...),
    description: str | None = Form(None),
    start_time: datetime=Form(...),
    end_time: datetime=Form(...),
    venue_id: int=Form(...),
    image: UploadFile | None = File(None),
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    data=EventCreate(
        title=title,
        description=description,
        start_time=start_time,
        end_time=end_time,
        create_at=datetime.utcnow(),
        venue_id=venue_id,
        image_url=None
    )
    service=EventService()
    event=service.create_event(db, data, image)
    return event

@router.get("/{event_id}", response_model=Event)
def get_event(
    event_id: int,
    db: Session = Depends(get_db),
):
    service=EventService()
    event=service.get_event(db, event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found",
        )
    return event