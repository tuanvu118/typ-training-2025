from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db,require_admin, require_self_or_admin
from app.schemas.order import OrderHoldRequest,OrderConfirmRequest
from app.Service.OrderService import OrderService

router = APIRouter()


@router.post("/hold")
def hold_tickets(
    data: OrderHoldRequest,
    db: Session = Depends(get_db),
    current_user=Depends(require_self_or_admin)
):
    return OrderService.hold_tickets(
        db=db,
        user_id=5,
        items=[item.dict() for item in data.items]
    )

@router.post("/confirm")
def confirm_order(
    data: OrderConfirmRequest,
    db: Session = Depends(get_db),
    current_user=Depends(require_self_or_admin)
):
    return OrderService.confirm_order(
        db=db,
        user_id=current_user.id,
        session_id=data.session_id,
        hold_token=data.hold_token
    )
