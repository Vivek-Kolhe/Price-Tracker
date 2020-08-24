import time
from notify import send_mail
from sites import *

urls = ["https://www.amazon.in/Sony-Bravia-Certified-Android-85X8000H/dp/B084T8MD67/ref=sr_1_4?dchild=1&pf_rd_i=1389396031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=596ea4be-20f6-4a22-bda9-d68047ac4236&pf_rd_r=GW9AJJTJP5V4RWGCK508&pf_rd_s=merchandised-search-14&pf_rd_t=101&qid=1595929056&refinements=p_36%3A7500000-&s=electronics&sr=1-4",
		"https://www.flipkart.com/apple-iphone-se-black-64-gb/p/itm832dd5963a08d?pid=MOBFRFXHCKWDAC4A&lid=LSTMOBFRFXHCKWDAC4AEQROVZ&marketplace=FLIPKART&srno=b_1_1&otracker=hp_rhs_announcement_1_4.rhsAnnouncement.RHS_ANNOUNCEMENT_NG7F2MMCSIA2&fm=neo%2Fmerchandising&iid=f808d16d-4ac1-4f4c-8cfb-5cbe7062eeb7.MOBFRFXHCKWDAC4A.SEARCH&ppt=browse&ppn=browse&ssid=lou82kspq80000001596274471278"
		] # product urls
marked_prices = [1000000, 100000] # Will notify if the items get below these prices, must pass prices corresponding to urls 
items = []

while True:
	for url in urls:
		if "flipkart" in url:
			flipkart(url, items)
		elif "amazon" in url:
			amazon(url, items)

	for i in range(len(items)):
		if items[i]["Price"] <= exp_prices[i]:
			msg = f"Price lowered for {items[i]['Title']} to Rs {items[i]['Price']}.\nGo check it out at {items[i]['Url']}"
			send_mail(msg)
			# print("done")
	time.sleep(6*3600)
	items.clear()
