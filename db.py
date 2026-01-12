import sqlite3

conn = sqlite3.connect("alerts.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    train_no TEXT,
    alert_type TEXT,
    alert_time TEXT,
    status TEXT
)
""")

conn.commit()
