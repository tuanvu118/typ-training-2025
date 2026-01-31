from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.ticketType import TicketTypeCreate, TicketType, TicketTypeResponse
from app.Service.TicketTypeService import TicketTypeService
from app.api.deps import get_db, require_admin

router = APIRouter()
service=TicketTypeService()

@router.post("/", response_model=TicketTypeCreate, status_code=status.HTTP_201_CREATED)
def create_ticket_type(
    data: TicketTypeCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    ticket_type = service.create_ticket_type(db, data)
    return ticket_type

@router.get("/{ticket_type_id}", response_model=TicketType)
def get_ticket_type(
    ticket_type_id: int,
    db: Session = Depends(get_db),
):
    ticket_type = service.get_ticket_type(db, ticket_type_id)
    if not ticket_type:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket type not found",
        )
    return ticket_type

@router.get("/", response_model=list[TicketType])
def list_ticket_types(  
    db: Session = Depends(get_db),
):
    ticket_types = service.list_ticket_types(db)
    return ticket_types

@router.delete("/{ticket_type_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ticket_type(
    ticket_type_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    ticket_type = service.get_ticket_type(db, ticket_type_id)
    if not ticket_type:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket type not found",
        )
    service.delete_ticket_type(db, ticket_type)


