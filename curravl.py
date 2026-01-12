from datetime import timedelta
import pytz

IST = pytz.timezone("Asia/Kolkata")

def calculate_current_booking_time(train_start_datetime):
    if train_start_datetime.tzinfo is None:
        train_start_datetime = IST.localize(train_start_datetime)
    else:
        train_start_datetime = train_start_datetime.astimezone(IST)

    return train_start_datetime - timedelta(hours=8)
