import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Only load dotenv for local development
try:
    from dotenv import load_dotenv
    load_dotenv()  # This will fail silently in GitHub Actions
except ImportError:
    pass  # In GitHub Actions, we don't need dotenv

def send_email(html):
    # Use os.environ.get() instead of os.getenv() as this will work in both local and GitHub Actions environments
    email_user = os.environ.get("EMAIL_USER") or os.getenv("EMAIL_USER")
    email_password = os.environ.get("EMAIL_PASSWORD") or os.getenv("EMAIL_PASSWORD")
    email_receiver = os.environ.get("EMAIL_RECEIVER") or os.getenv("EMAIL_RECEIVER")

    # Debug: Check if credentials are set
    print(f"EMAIL_USER set: {bool(email_user)}")
    print(f"EMAIL_PASSWORD set: {bool(email_password)}")
    print(f"EMAIL_RECEIVER set: {bool(email_receiver)}")

    # Validate credentials
    if not all([email_user, email_password, email_receiver]):
        missing = []
        if not email_user: missing.append("EMAIL_USER")
        if not email_password: missing.append("EMAIL_PASSWORD")
        if not email_receiver: missing.append("EMAIL_RECEIVER")
        raise ValueError(f"Missing credentials: {', '.join(missing)}")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Iyaji's Daily Interest News"
    msg["From"] = email_user
    msg["To"] = email_receiver
    msg.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(email_user, email_password)
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise
