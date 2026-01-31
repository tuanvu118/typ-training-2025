# app/core/redis_expire_listener.py
import json
import redis

r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    db=0,
    decode_responses=True
)

pubsub = r.pubsub()
pubsub.psubscribe("__keyevent@0__:expired")

print("Redis expire listener started")

for msg in pubsub.listen():
    if msg["type"] != "pmessage":
        continue

    expired_key = msg["data"]

    if not expired_key.startswith("ticket_hold:"):
        continue

    session_id = expired_key.split(":")[-1]
    hold_stock_key = f"ticket_hold_stock:{session_id}"

    data = r.get(hold_stock_key)
    if not data:
        continue

    deducted = json.loads(data)
    for ticket_type_id, qty in deducted:
        r.incrby(f"ticket_stock:{ticket_type_id}", qty)

    r.delete(hold_stock_key)
    print(f" Released stock for session {session_id}")

