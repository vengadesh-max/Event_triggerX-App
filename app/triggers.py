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


# Endpoint to create a trigger
@router.post("/", response_model=schemas.TriggerResponse)
def create_trigger(trigger: schemas.TriggerCreate, db: Session = Depends(get_db)):
    return crud.create_trigger(db=db, trigger_data=trigger)


# Endpoint to get all triggers
@router.get("/", response_model=list[schemas.TriggerResponse])
def get_triggers(db: Session = Depends(get_db)):
    return crud.get_all_triggers(db=db)


# Endpoint to delete a trigger
@router.delete("/{trigger_id}")
def delete_trigger(trigger_id: int, db: Session = Depends(get_db)):
    crud.delete_trigger(db=db, trigger_id=trigger_id)
    return {"message": "Trigger deleted successfully"}
