from fastapi import FastAPI, HTTPException
from models import AlertRequest
from tatkal import calculate_tatkal_time
from database import alerts_db

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

        alerts_db.append({
            "email": alert.user_email,
            "train": alert.train_no,
            "journey_date": alert.journey_date,
            "class": alert.travel_class,
            "alert_type": alert.alert_type,
            "alert_time": tatkal_time
        })

        return {
            "message": "Tatkal alert created",
            "tatkal_time": tatkal_time
        }

    else:
        raise HTTPException(
            status_code=400,
            detail="Only Tatkal supported on Day 1"
        )
