import requests

# get method
s = requests.get("https://financialmodelingprep.com/api/v3/quote/AAPL?apikey=demo")
# This function print the what is inside this url request content
print(s.text)

print(s.status_code)

"""
For more information about status code visit this website
https://developer.amazon.com/docs/amazon-drive/ad-restful-api-response-codes.html
"""
# post method
"""
# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)
in post method we want to send some data on website 
this method is secure
"""


