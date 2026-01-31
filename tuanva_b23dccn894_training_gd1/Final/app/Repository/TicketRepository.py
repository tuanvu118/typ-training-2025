from sqlalchemy.orm import Session
from app.models.ticket import Ticket

class TicketRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> Ticket:
        ticket = Ticket(**data)
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket
