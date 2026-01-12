from pydantic import BaseModel
from datetime import date, datetime

class AlertRequest(BaseModel):
    user_email: str
    train_no: str
    journey_date: date
    travel_class: str
    alert_type: str  # TATKAL / CURRENT_BOOKING
    train_start_time: datetime | None = None
