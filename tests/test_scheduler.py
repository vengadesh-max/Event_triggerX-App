import pytest
from datetime import datetime, timedelta
from app.scheduler import schedule_trigger
from app.database import get_db


# Mock database session
@pytest.fixture
def db_session():
    from sqlalchemy.orm import sessionmaker
    from app.database import engine

    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


# Test: Schedule a one-time trigger
def test_schedule_one_time_trigger(db_session):
    trigger_time = datetime.utcnow() + timedelta(minutes=1)
    trigger_data = {
        "name": "One-Time Trigger",
        "trigger_type": "scheduled",
        "schedule_time": trigger_time,
        "interval_seconds": None,
    }
    result = schedule_trigger(trigger_data, db_session)
    assert result is not None
    assert result.name == "One-Time Trigger"


# Test: Schedule a recurring trigger
def test_schedule_recurring_trigger(db_session):
    trigger_data = {
        "name": "Recurring Trigger",
        "trigger_type": "scheduled",
        "schedule_time": None,
        "interval_seconds": 300,
    }
    result = schedule_trigger(trigger_data, db_session)
    assert result is not None
    assert result.name == "Recurring Trigger"
    assert result.interval_seconds == 300
