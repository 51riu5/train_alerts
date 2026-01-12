from datetime import datetime
from db import cursor
from scheduler import schedule_alert

def restore_pending_alerts():
    cursor.execute(
        "SELECT id, email, train_no, alert_time FROM alerts WHERE status='PENDING'"
    )

    rows = cursor.fetchall()
    for alert_id, email, train_no, alert_time in rows:
        alert_time = datetime.fromisoformat(alert_time)

        if alert_time > datetime.now(alert_time.tzinfo):
            schedule_alert(alert_id, alert_time, email, train_no)
