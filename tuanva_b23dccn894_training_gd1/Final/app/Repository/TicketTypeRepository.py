from sqlalchemy.orm import Session
from app.models.ticketType import TicketType
from app.schemas.ticketType import TicketTypeCreate, TicketTypeUpdate

class TicketTypeRepository:
    def create(self, db: Session, data: TicketTypeCreate) -> TicketType:
        ticket_type = TicketType(**data.dict())
        db.add(ticket_type)
        db.commit()
        db.refresh(ticket_type)
        return ticket_type
    
    def get_by_id(self,db: Session, ticket_type_id: int) -> TicketType | None:
        return db.query(TicketType).filter(TicketType.id == ticket_type_id).first() 

    def update(self, db: Session, ticket_type: TicketType, data: TicketTypeUpdate) -> TicketType:
        for field, value in data.dict(exclude_unset=True).items():
            setattr(ticket_type, field, value)
        db.commit() 
        db.refresh(ticket_type)
        return ticket_type
    
    def delete(self, db: Session, ticket_type: TicketType) -> None:
        db.delete(ticket_type)
        db.commit()

    def list_by_event(self, db: Session, event_id: int) -> list[TicketType]:
        return db.query(TicketType).filter(TicketType.event_id == event_id).all()
    
    def list_all(self, db: Session) -> list[TicketType]:
        return db.query(TicketType).all()