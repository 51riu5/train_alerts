from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

scheduler = BackgroundScheduler()
scheduler.start()

def send_alert(email, message):
    print(f"🚨 ALERT for {email}: {message}")

def schedule_alert(run_time: datetime, email: str, message: str):
    scheduler.add_job(
        send_alert,
        trigger="date",
        run_date=run_time,
        args=[email, message]
    )
