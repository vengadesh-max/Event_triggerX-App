from datetime import datetime
from typing import Any
import json


def format_datetime(dt: datetime) -> str:
    """Convert datetime to string format."""
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def parse_json(payload: Any) -> dict:
    """Utility function to parse JSON payload."""
    return json.loads(payload) if isinstance(payload, str) else payload
