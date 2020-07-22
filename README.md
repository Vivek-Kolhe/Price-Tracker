# Price-Tracker
Simple python program to track prices on Amazon.

# Usage
Get your account id and auth token from [Twilio](https://www.twilio.com/).\
Verify your mobile number in Twilio and make changes in the code accordingly.

# Requirements
Requests
```
pip3 install requests
```
BeautifulSoup4
```
pip3 install bs4
```
Twilio
```
pip3 install twilio
```
*Note : Currently works for single product only and won't work for **deal prices**. Also twilio trial account lets you send SMS 15 - 16 times only. Will change it to E-mail next time. :)* 
