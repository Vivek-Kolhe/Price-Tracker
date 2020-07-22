import requests
from bs4 import BeautifulSoup
from twilio.rest import Client


USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
headers = {"user-agent" : USER_AGENT}
url = "" # pass the url of amazon product
account_sid = "" # account id from twilio
auth_token = "" # twilio auth token

exp_price = float(input("Will notify you if price gets below: "))

response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.content, "html.parser")
title = soup.find(id = "productTitle").get_text().strip()
price = soup.find(id = "priceblock_ourprice").get_text().strip()
price = float(price[2:].replace(",", ""))
# print(title, price)

def send_update(account_sid, auth_token, title, price):
	client = Client(account_sid, auth_token) 
	body = f"Hey, price for {title} has been lowered to {price}."
	message = client.messages.create( 
	                              from_='', # your twilio phone number
	                              body = body,        
	                              to='' # your actual phone number
	                          		) 
 
	return message.sid

if price < exp_price:
	print(send_update(account_sid, auth_token, title, price))