from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, JSON
from app.base import Base
from datetime import datetime


# Trigger Model
class Trigger(Base):
    __tablename__ = "triggers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    trigger_type = Column(String)
    schedule_time = Column(DateTime)
    interval_seconds = Column(Integer)
    api_payload = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)


# EventLog Model
class EventLog(Base):
    __tablename__ = "event_logs"
    id = Column(Integer, primary_key=True, index=True)
    trigger_id = Column(Integer, index=True)
    event_type = Column(String)
    payload = Column(JSON)
    triggered_at = Column(DateTime, default=datetime.utcnow)
    archived_at = Column(DateTime)
    deleted_at = Column(DateTime)
