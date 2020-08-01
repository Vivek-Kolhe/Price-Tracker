# Price-Tracker
Simple python program to track prices on Amazon and Flipkart.

# Usage
Fork the repository.\
Commit changes in ***notify.py*** and ***main.py***
- notify.py
1) Line 7\
``` email["to] = "<your gmail account here>"```
2) Line 15\
```smtp.login("xyz@gmail.com", "password") # another gmail account to send mails```
- main.py
1) Pass urls in line 5
2) Prices in ```exp_prices```

```
urls = [
        "https://www.amazon.in/product1/",
        "https://www.flipkart.in/product2/"
       ] # url as strings
exp_prices = [1000, 500] # as integer or float type
```
Here, it'll notify you when price for product1 gets below ***1000*** and same for product2 when it gets below ***500***.

Turn on [Less Secure Apps](https://myaccount.google.com/lesssecureapps) from your another gmail account and run the code.\
Check the mail entered on line 7 in *notify.py* for e-mails.
