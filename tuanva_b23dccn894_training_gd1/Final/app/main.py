from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.endpoints import  user, auth, VenueController, EventController, TicketTypeController, OrderController

app=FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application with static file serving.",
    version="1.0.0"
)
#Include routes
app.include_router(user.router, prefix="/users", tags=["users"])    
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(VenueController.router, prefix="/venues", tags=["venues"])
app.include_router(EventController.router, prefix="/events", tags=["events"])
app.include_router(TicketTypeController.router, prefix="/ticket-types", tags=["ticket-types"])
app.include_router(OrderController.router,prefix="/order",tags=["order"])

@app.get("/")#127.0.0.1:8000/
def read_root():
    return {"message": "Welcome to My FastAPI Application!"}
