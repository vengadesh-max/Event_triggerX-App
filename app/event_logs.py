from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter()


# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint to log an event
@router.post("/", response_model=schemas.EventLogResponse)
def log_event(event: schemas.EventLogCreate, db: Session = Depends(get_db)):
    return crud.log_event(
        db=db,
        trigger_id=event.trigger_id,
        event_type=event.event_type,
        payload=event.payload,
    )


# Endpoint to retrieve active event logs
@router.get("/", response_model=list[schemas.EventLogResponse])
def get_active_event_logs(db: Session = Depends(get_db)):
    return crud.get_active_event_logs(db=db)


# Endpoint to delete expired event logs
@router.delete("/expired")
def delete_expired_event_logs(db: Session = Depends(get_db)):
    return crud.delete_expired_event_logs(db=db)
