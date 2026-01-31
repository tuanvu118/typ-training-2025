from pydantic import BaseModel

class OrderItemBase(BaseModel):
    order_id: int
    ticket_type_item_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemUpdate(BaseModel):
    pass

class OrderItemInDBBase(OrderItemBase):
    id: int

    class Config:
        orm_mode = True
class OrderItem(OrderItemInDBBase):
    pass