import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.message import EmailMessage

urls = ["https://www.amazon.in/Test-Exclusive-547/dp/B078BNQ318/ref=pd_lpo_107_t_1/259-7042788-8081138?_encoding=UTF8&pd_rd_i=B078BNQ318&pd_rd_r=18883baa-d31a-48c1-afb9-efaae994b163&pd_rd_w=sC6sf&pd_rd_wg=GCLUL&pf_rd_p=5a903e39-3cff-40f0-9a69-33552e242181&pf_rd_r=C6S449FK1YR9WYB4ZGRE&psc=1&refRID=C6S449FK1YR9WYB4ZGRE",
		"https://www.amazon.in/MSI-GF65-Thin-9SEXR-438IN-9S7-16W112-438/dp/B08699BD7L/ref=sr_1_13_sspa?crid=GPDSCPI2C7ZA&dchild=1&keywords=nvidia+rtx+2080+super&qid=1595584486&s=electronics&sprefix=nvidia+%2Celectronics%2C1149&sr=1-13-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTEVHOEpDMEpGV05GJmVuY3J5cHRlZElkPUEwMDc4Mjk5M0VKSDhSMkVVUUVaNyZlbmNyeXB0ZWRBZElkPUExMDQ4Mzc2M0RMV0hVRDFEM0hUSCZ3aWRnZXROYW1lPXNwX210ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
		"https://www.amazon.in/Intel-Core-i9-7900X-Processor/dp/B072KTSCCS/ref=sr_1_4?dchild=1&keywords=intel+i9&qid=1595584173&sr=8-4"
		] # product urls
exp_prices = [] # Will notify if the items get below these prices, must enter corresponding to urls
items = []

def get_item(urls, items):
	USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
	headers = {"user-agent" : USER_AGENT}
	for url in urls:
		response = requests.get(url, headers = headers)
		soup = BeautifulSoup(response.content, "html.parser")
		title = soup.find(id = "productTitle").get_text().strip()
		price = soup.find(id = "priceblock_ourprice").get_text().strip()
		price = float(price[2:].replace(",", ""))
		items.append({"Title" : title, "Price" : price, "Url" : url})
		# print("all done!")

def send_mail(msg):
    email = EmailMessage()
    email["from"] = "Tracker Bot"
    email["to"] = "" # your gmail account on which on you want notifications
    email["subject"] = "Price Lowered"

    email.set_content(msg)

    with smtplib.SMTP(host = "smtp.gmail.com", port = 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("", "") # login your dummy/fake account in this format ("xyz@gmail.com", "password")
        smtp.send_message(email)

get_item(urls, items)

while True:
	for i in range(len(items)):
		if items[i]["Price"] < exp_prices[i]:
			msg = f"Price has lowered for {items[i]['Title']} to {items[i]['Price']}.\nGo check it out at {items[i]['Url']}"
			send_mail(msg)
			# print("done")
	time.sleep(6*3600)
