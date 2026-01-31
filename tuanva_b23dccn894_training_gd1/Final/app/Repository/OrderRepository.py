from sqlalchemy.orm import Session
from app.models.order import Order

class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> Order:
        order = Order(**data)
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order
