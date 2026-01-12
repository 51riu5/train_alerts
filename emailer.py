import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "rishitmenon0@gmail.com"
EMAIL_PASSWORD = "ftovwkdfyqffeudr"  # Gmail App Password

def send_email(to_email, subject, body):
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
