from pydantic import BaseModel
from datetime import date

class AlertRequest(BaseModel):
    user_email: str
    train_no: str
    journey_date: date
    travel_class: str  # 1A, 2A, 3A, SL, 2S
    alert_type: str    # TATKAL or CURRENT_BOOKING
