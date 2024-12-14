from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# Trigger Create/Update schemas
class TriggerBase(BaseModel):
    name: str
    trigger_type: str
    schedule_time: datetime
    interval_seconds: int
    api_payload: dict


class TriggerCreate(TriggerBase):
    pass


class TriggerUpdate(TriggerBase):
    pass


# Trigger Response Schema
class TriggerResponse(TriggerBase):
    id: int
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Config:
        from_attributes = True


# EventLog Create/Response schemas
class EventLogCreate(BaseModel):
    trigger_id: int
    event_type: str
    payload: dict


class EventLogResponse(EventLogCreate):
    id: int
    triggered_at: datetime
    archived_at: datetime
    deleted_at: datetime

    class Config:
        from_attributes = True
