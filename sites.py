import requests
from bs4 import BeautifulSoup

def flipkart(url, items):
	USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
	headers = {"user-agent" : USER_AGENT}
	response = requests.get(url, headers = headers)
	soup = BeautifulSoup(response.content, "html.parser")
	title = soup.find(class_ = "_35KyD6").get_text().strip()
	price = soup.find(class_ = "_1vC4OE _3qQ9m1").get_text().strip()
	price = float(price[1:].replace(",", ""))
	items.append({"Title" : title, "Price" : price, "Url" : url})

def amazon(url, items):
	USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
	headers = {"user-agent" : USER_AGENT}
	response = requests.get(url, headers = headers)
	soup = BeautifulSoup(response.content, "html.parser")
	title = soup.find(id = "productTitle").get_text().strip()
	price = soup.find(id = "priceblock_ourprice")
	if price != None:
		price = price.get_text().strip()
		price = float(price[2:].replace(",", ""))
	deal_price = soup.find(id = "priceblock_dealprice")
	if deal_price != None:
		deal_price = deal_price.get_text().strip()
		deal_price = float(deal_price[2:].replace(",", ""))

	if price == None:
		items.append({"Title" : title, "Price" : deal_price, "Url" : url})
	else:
		items.append({"Title" : title, "Price" : price, "Url" : url})