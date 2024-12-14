# app/__init__.py

from fastapi import FastAPI
from app.database import init_db

# Initialize the database
init_db()

# Create FastAPI instance
app = FastAPI(title="Event Trigger Platform", version="1.0.0")


# Initialize the database (optional, if necessary on startup)
@app.on_event("startup")
async def startup_event():
    init_db()  # Example: Initialize the database connection or perform migrations


# Import and include routers if any
from app.routes import trigger_router, event_router

app.include_router(trigger_router, prefix="/api/triggers", tags=["Triggers"])
app.include_router(event_router, prefix="/api/events", tags=["Events"])
