from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from  app.api.deps import get_db
from app.Service.VenueService import VenueService
from app.schemas.venue import VenueResponse, VenueCreate, VenueUpdate
from app.api.deps import require_admin

router = APIRouter()
venue_service = VenueService()

@router.get("/", response_model = List[VenueResponse])
def list_venues(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    return venue_service.list_venues(db, skip, limit)


@router.get("/{venue_id}", response_model= VenueResponse )
def get_venue(
    venue_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    return venue_service.get_venue(db, venue_id)

@router.post("/", response_model=VenueResponse)
def create_venue(
    venue_in: VenueCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    return venue_service.create(db, venue_in)

@router.put("/{venue_id}", response_model=VenueResponse)
def update_venue(
    venue_id: int,
    venue_in: VenueUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    return venue_service.update_venue(db, venue_id, venue_in)   

@router.delete("/{venue_id}", status_code=204)
def delete_venue(
    venue_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    venue_service.delete_venue(db, venue_id)
