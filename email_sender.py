import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from dotenv import load_dotenv

load_dotenv()


def send_email(html):

    msg = MIMEMultipart("alternative")

    msg["Subject"] = "Iyaji's Daily Interest News"

    msg["From"] = os.getenv("EMAIL_USER")

    msg["To"] = os.getenv("EMAIL_RECEIVER")

    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()

        smtp.login(
            os.getenv("EMAIL_USER"),
            os.getenv("EMAIL_PASSWORD")
        )

        smtp.send_message(msg)
