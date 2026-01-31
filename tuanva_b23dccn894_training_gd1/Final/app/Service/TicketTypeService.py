from sqlalchemy.orm import Session
from app.schemas.ticketType import TicketTypeCreate, TicketTypeUpdate, TicketType
from app.Repository.TicketTypeRepository import TicketTypeRepository

repo=TicketTypeRepository()

class TicketTypeService:
    def create_ticket_type(self, db: Session, data: TicketTypeCreate) -> TicketType:
        return repo.create(db, data)
    
    def get_ticket_type(self, db: Session, ticket_type_id: int) -> TicketType | None:
        return repo.get_by_id(db, ticket_type_id)
    
    def update_ticket_type(self, db: Session, ticket_type_id: int, data: TicketTypeUpdate) -> TicketType | None:
        ticket_type = repo.get_by_id(db, ticket_type_id)
        if not ticket_type:
            return None
        return repo.update(db, ticket_type, data)
    
    def delete_ticket_type(self, db: Session, ticket_type_id: int) -> bool:
        ticket_type = repo.get_by_id(db, ticket_type_id)
        if not ticket_type:
            return False
        repo.delete(db, ticket_type)
        return True
    
    def list_ticket_types_by_event(self, db: Session, event_id: int) -> list[TicketType]:
        return repo.list_by_event(db, event_id)
    
    def list_ticket_types(self, db: Session) -> list[TicketType]:
        return repo.list_all(db)