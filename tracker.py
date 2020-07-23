import requests
import smtplib
from email.message import EmailMessage
from bs4 import BeautifulSoup

USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
headers = {"user-agent" : USER_AGENT}
url = "" # pass the url of amazon product

exp_price = float(input("Will notify you if price gets below: "))

response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.content, "html.parser")
title = soup.find(id = "productTitle").get_text().strip()
price = soup.find(id = "priceblock_ourprice").get_text().strip()
price = float(price[2:].replace(",", ""))
# print(title, price)

def send_mail(title, price, url):
    email = EmailMessage()
    email["from"] = "Tracker Bot"
    email["to"] = "" # your gmail account on which on you want notifications
    email["subject"] = "Price for your products lowered."

    email.set_content(f"Price lowered of {title} to {price}.\nGo check it out on {url}.")

    with smtplib.SMTP(host = "smtp.gmail.com", port = 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("", "") # login your dummy/fake account in this format ("xyz@gmail.com", "password")
        smtp.send_message(email)

if exp_price < price:
    send_mail(title, price, url)
