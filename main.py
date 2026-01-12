from fastapi import FastAPI, HTTPException
from models import AlertRequest
from tatkal import calculate_tatkal_time
from curravl import calculate_current_booking_time
from scheduler import schedule_alert 
from datetime import datetime


app = FastAPI(title="Train Booking Alert System")

@app.get("/")
def root():
    return {"status": "Train Alert API running"}

@app.post("/create-alert/")
def create_alert(alert: AlertRequest):

    if alert.alert_type == "TATKAL":
        tatkal_time = calculate_tatkal_time(
            alert.journey_date,
            alert.travel_class
        )


        if cb_time <= datetime.now(cb_time.tzinfo):
            raise HTTPException(
        status_code=400,
        detail="Alert time is in the past"
    )


        schedule_alert(
            tatkal_time,
            alert.user_email,
            f"Tatkal booking OPEN for Train {alert.train_no}"
        )

        return {
            "message": "Tatkal alert scheduled",
            "alert_time": tatkal_time
        }

    elif alert.alert_type == "CURRENT":

        if not alert.train_start_time:
            raise HTTPException(
                status_code=400,
                detail="train_start_time required for current booking"
            )

        cb_time = calculate_current_booking_time(
            alert.train_start_time
        )

        

        schedule_alert(
            cb_time,
            alert.user_email,
            f"Current Booking OPEN for Train {alert.train_no}"
        )

        return {
            "message": "Current booking alert scheduled",
            "alert_time": cb_time
        }

    else:
        raise HTTPException(status_code=400, detail="Invalid alert type")
