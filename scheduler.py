from apscheduler.schedulers.background import BackgroundScheduler
from emailer import send_email
from db import conn, cursor

scheduler = BackgroundScheduler()
scheduler.start()
print("✅ Scheduler started")

def send_alert(alert_id, email, train_no):
    send_email(
        email,
        "🚆 Train Booking Alert",
        f"Current Booking OPEN for Train {train_no}"
    )

    cursor.execute(
        "UPDATE alerts SET status='SENT' WHERE id=?",
        (alert_id,)
    )
    conn.commit()

def schedule_alert(alert_id, run_time, email, train_no):
    scheduler.add_job(
        send_alert,
        trigger="date",
        run_date=run_time,
        args=[alert_id, email, train_no]
    )
