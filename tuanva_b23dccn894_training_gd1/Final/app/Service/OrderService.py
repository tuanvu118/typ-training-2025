import uuid, json
from sqlalchemy.orm import Session
from app.core.redis import redis_client
from app.Repository.TicketTypeRepository import TicketTypeRepository
from app.Repository.OrderRepository import OrderRepository
from app.Repository.OrderItemRepository import OrderItemRepository
from app.Repository.TicketRepository import TicketRepository
from app.schemas.order import OrderCreate
from app.schemas.ticket import TicketCreate

HOLD_TTL = 120
    
ticketTypeRepo = TicketTypeRepository()


class OrderService:
    @staticmethod
    def hold_tickets(db: Session, user_id: int, items: list[dict]):
        session_id = str(uuid.uuid4())
        hold_token = str(uuid.uuid4())

        # để rollback nếu fail giữa chừng
        deducted = []  # list[(ticket_type_id, quantity)]

        try:
            for item in items:
                ticket_type_id = item["ticket_type_id"]
                qty = item["quantity"]

                stock_key = f"ticket_stock:{ticket_type_id}"

                # Init stock nếu chưa có (an toàn hơn: SETNX)
                if not redis_client.exists(stock_key):
                    ticket_type = ticketTypeRepo.get_by_id(db,ticket_type_id)
                    if not ticket_type:
                        raise Exception(f"TicketType {ticket_type_id} not found")
                    # tránh race init: setnx
                    redis_client.setnx(stock_key, int(ticket_type.total_quantity))

                remain = redis_client.decrby(stock_key, qty)
                if remain < 0:
                    # hoàn lại cái vừa trừ
                    redis_client.incrby(stock_key, qty)
                    raise Exception("Sold out")

                deducted.append((ticket_type_id, qty))

            hold_key = f"ticket_hold:{user_id}:{session_id}"
            hold_stock_key = f"ticket_hold_stock:{session_id}"
            redis_client.setex(
                hold_key,
                HOLD_TTL,
                json.dumps({"items": items, "token": hold_token})
            )
            redis_client.setex(
                hold_stock_key,
                HOLD_TTL + 30,
                json.dumps(deducted)
            )

            return {"session_id": session_id, "hold_token": hold_token, "expire_in": HOLD_TTL}

        except Exception:
            # rollback toàn bộ các loại vé đã trừ trước đó
            for ticket_type_id, qty in deducted:
                redis_client.incrby(f"ticket_stock:{ticket_type_id}", qty)
            raise

    @staticmethod
    def confirm_order(db: Session, user_id: int, session_id: str, hold_token: str):
        hold_key = f"ticket_hold:{user_id}:{session_id}"
        raw = redis_client.get(hold_key)
        if not raw:
            hold_stock_key = f"ticket_hold_stock:{session_id}"
            data = redis_client.get(hold_stock_key)
            if data:
                deducted = json.loads(data)
                for ticket_type_id,qty in deducted:
                    redis_client.incrby(f"ticket_stock:{ticket_type_id}",qty)
                redis_client.delete(hold_stock_key)
            
            raise Exception("Hold expired")

        payload = json.loads(raw)
        if payload["token"] != hold_token:
            raise Exception("Invalid hold token")

        items = payload["items"]

        # tính tổng tiền
        total_amount = 0
        ticket_type_map = {}  # cache ticket_type để dùng lại
        for item in items:
            tt_id = item["ticket_type_id"]
            ticket_type = ticketTypeRepo.get_by_id(db,tt_id)
            if not ticket_type:
                raise Exception(f"TicketType {tt_id} not found")
            ticket_type_map[tt_id] = ticket_type
            total_amount += ticket_type.price * item["quantity"]

        try:
            # 1) Create Order
            order_repo = OrderRepository(db)

            order = order_repo.create({
                "user_id": user_id,
                "total_amount": total_amount,
                "status": "completed"
            })


            order_item_repo = OrderItemRepository(db)
            ticket_repo = TicketRepository(db)

            # 2) Create OrderItem + Ticket
            for item in items:
                tt_id = item["ticket_type_id"]
                qty = item["quantity"]
                ticket_type = ticket_type_map[tt_id]

                ticket_type.total_quantity-=qty

                #  Create OrderItem
                order_item_repo.create({
                    "order_id": order.id,
                    "ticket_type_item_id": tt_id,
                    "quantity": qty
                })

                # Create Ticket (1 record / 1 vé)
                for _ in range(qty):
                    ticket_repo.create({
                        "event_id": ticket_type.event_id,
                        "ticket_type_id": tt_id,
                        "user_id": user_id,
                        "order_id": order.id,
                        "status": "confirmed"
                    })

            # 3) Xoá hold key sau khi DB ok
            redis_client.delete(hold_key)
            redis_client.delete(f"ticket_hold_stock:{session_id}")
            return order

        except Exception:
            # nếu DB fail thì rollback DB (tuỳ cách bạn quản lý session)
            db.rollback()
            raise
