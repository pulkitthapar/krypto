#MADE FOR STORING ALL TOKENS IN A DICTIONARY

# import requests
# import smtplib
# import time
# import json

# #//////////////////////////////////////////////////  Enter URL  /////////////////////////////////////////////////////////////////////////

# url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# token = input("Name of token: ").strip().lower()
# response = json.loads(requests.get(url).text)
# curr=dict()
# for i in range(len(response)):
#     curr[response[i]['id']]=i
# x=curr[token]
# print(f"Current price: {str(response[x]['current_price'])} USD")
# target=int(input("Target price: "))

# def fetch_price(token):
#     url2 = (f"https://api.coingecko.com/api/v3/simple/price?ids={token}&vs_currencies=usd")
