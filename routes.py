from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, init_db
from app.models import Trigger, EventLog
from app.schemas import TriggerCreate, EventLogResponse
from datetime import datetime, timedelta

# Initialize database (create tables if not already created)
init_db()


# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Routers
trigger_router = APIRouter()
event_router = APIRouter()


# Trigger API Endpoints
@trigger_router.post("/triggers/", status_code=status.HTTP_201_CREATED)
def create_trigger(trigger: TriggerCreate, db: Session = Depends(get_db)):
    """
    Create a new trigger: Scheduled or API-based.
    """
    new_trigger = Trigger(**trigger.dict(), created_at=datetime.now())
    db.add(new_trigger)
    db.commit()
    db.refresh(new_trigger)
    return {"message": "Trigger created successfully", "trigger": new_trigger}


@trigger_router.get("/triggers/", response_model=list[TriggerCreate])
def get_triggers(db: Session = Depends(get_db)):
    """
    Retrieve all active triggers.
    """
    triggers = db.query(Trigger).all()
    return triggers


@trigger_router.delete("/triggers/{trigger_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_trigger(trigger_id: int, db: Session = Depends(get_db)):
    """
    Delete a trigger by ID.
    """
    trigger = db.query(Trigger).filter(Trigger.id == trigger_id).first()
    if not trigger:
        raise HTTPException(status_code=404, detail="Trigger not found")
    db.delete(trigger)
    db.commit()
    return {"message": "Trigger deleted successfully"}


# Event Log Endpoints
@event_router.get("/events/", response_model=list[EventLogResponse])
def get_active_events(db: Session = Depends(get_db)):
    """
    Retrieve all events triggered in the last 2 hours.
    """
    two_hours_ago = datetime.now() - timedelta(hours=2)
    active_events = (
        db.query(EventLog).filter(EventLog.created_at >= two_hours_ago).all()
    )
    return active_events


@event_router.get("/events/archived", response_model=list[EventLogResponse])
def get_archived_events(db: Session = Depends(get_db)):
    """
    Retrieve archived events that are older than 2 hours but not deleted.
    """
    two_hours_ago = datetime.now() - timedelta(hours=2)
    archived_events = (
        db.query(EventLog)
        .filter(
            EventLog.created_at < two_hours_ago,
            EventLog.created_at >= two_hours_ago - timedelta(hours=46),
        )
        .all()
    )
    return archived_events
