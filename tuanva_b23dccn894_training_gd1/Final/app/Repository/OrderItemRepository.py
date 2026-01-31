from sqlalchemy.orm import Session
from app.models.OrderItem import OrderItem

class OrderItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> OrderItem:
        order_item = OrderItem(**data)
        self.db.add(order_item)
        self.db.commit()
        self.db.refresh(order_item)
        return order_item
