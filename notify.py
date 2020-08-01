import smtplib
from email.message import EmailMessage

def send_mail(msg):
    email = EmailMessage()
    email["from"] = "Tracker Bot"
    email["to"] = "" # your gmail account on which on you want notifications
    email["subject"] = "Price Lowered"

    email.set_content(msg)

    with smtplib.SMTP(host = "smtp.gmail.com", port = 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("", "") # login your another gmail account in this format ("xyz@gmail.com", "password")
        smtp.send_message(email)