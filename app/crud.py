from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timedelta
from app.models import Trigger, EventLog
from app.schemas import TriggerCreate, TriggerUpdate
from fastapi import HTTPException


# Create a new trigger
def create_trigger(db: Session, trigger_data: TriggerCreate):
    try:
        new_trigger = Trigger(
            name=trigger_data.name,
            trigger_type=trigger_data.trigger_type,
            schedule_time=trigger_data.schedule_time,
            interval_seconds=trigger_data.interval_seconds,
            api_payload=trigger_data.api_payload,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            is_active=True,
        )
        db.add(new_trigger)
        db.commit()
        db.refresh(new_trigger)
        return new_trigger
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error creating trigger")


# Get a trigger by ID
def get_trigger_by_id(db: Session, trigger_id: int):
    trigger = db.query(Trigger).filter(Trigger.id == trigger_id).first()
    if not trigger:
        raise HTTPException(status_code=404, detail="Trigger not found")
    return trigger


# Get all triggers
def get_all_triggers(db: Session):
    return db.query(Trigger).all()


# Update an existing trigger
def update_trigger(db: Session, trigger_id: int, trigger_data: TriggerUpdate):
    try:
        trigger = db.query(Trigger).filter(Trigger.id == trigger_id).first()
        if not trigger:
            raise HTTPException(status_code=404, detail="Trigger not found")

        # Update fields dynamically
        update_data = trigger_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(trigger, key, value)

        trigger.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(trigger)
        return trigger
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error updating trigger")


# Delete a trigger
def delete_trigger(db: Session, trigger_id: int):
    try:
        trigger = db.query(Trigger).filter(Trigger.id == trigger_id).first()
        if not trigger:
            raise HTTPException(status_code=404, detail="Trigger not found")

        db.delete(trigger)
        db.commit()
        return {"message": "Trigger deleted successfully"}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error deleting trigger")


# Log an event
def log_event(db: Session, trigger_id: int, event_type: str, payload: dict):
    try:
        new_event = EventLog(
            trigger_id=trigger_id,
            event_type=event_type,
            payload=payload,
            triggered_at=datetime.utcnow(),
            archived_at=datetime.utcnow() + timedelta(hours=2),
            deleted_at=datetime.utcnow() + timedelta(hours=48),
        )
        db.add(new_event)
        db.commit()
        db.refresh(new_event)
        return new_event
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error logging event")


# Retrieve active event logs
def get_active_event_logs(db: Session):
    try:
        current_time = datetime.utcnow()
        active_logs = (
            db.query(EventLog)
            .filter(
                EventLog.triggered_at <= current_time,
                EventLog.archived_at > current_time,
            )
            .all()
        )
        return active_logs
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error retrieving active logs")


# Retrieve archived event logs
def get_archived_event_logs(db: Session):
    try:
        current_time = datetime.utcnow()
        archived_logs = (
            db.query(EventLog)
            .filter(
                EventLog.archived_at <= current_time, EventLog.deleted_at > current_time
            )
            .all()
        )
        return archived_logs
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error retrieving archived logs")


# Delete expired event logs
def delete_expired_event_logs(db: Session):
    try:
        current_time = datetime.utcnow()
        expired_logs = db.query(EventLog).filter(EventLog.deleted_at <= current_time)
        deleted_count = expired_logs.delete(synchronize_session=False)
        db.commit()
        return {"deleted_logs_count": deleted_count}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error deleting expired logs")


# def get_active_event_logs(db: Session):
#     try:
#         current_time = datetime.utcnow()  # Get the current UTC time
#         active_logs = (
#             db.query(EventLog)
#             .filter(
#                 EventLog.triggered_at <= current_time,  # Event has been triggered
#                 EventLog.archived_at > current_time,  # Event is not yet archived
#             )
#             .all()
#         )
#         return active_logs
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Error retrieving active logs")


# def delete_expired_event_logs(db: Session):
#     try:
#         current_time = datetime.utcnow()  # Get the current UTC time
#         expired_logs = db.query(EventLog).filter(EventLog.deleted_at <= current_time)
#         deleted_count = expired_logs.delete(
#             synchronize_session=False
#         )  # Delete expired logs
#         db.commit()  # Commit the transaction to apply the changes
#         return {"deleted_logs_count": deleted_count}  # Return count of deleted logs
#     except Exception as e:
#         db.rollback()  # Rollback in case of error to maintain database consistency
#         raise HTTPException(status_code=500, detail="Error deleting expired logs")
