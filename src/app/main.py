import ccxt
import numpy as np
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from api_key import API_KEY

#42c66e46-087e-452b-80cc-e456b17e9cbf
#https://coinmarketcap.com/currencies/bitcoin/

url = 'https://pro-api.coinmarketcap.com//v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'50',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEY,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  """with open("price_file.json", 'w', encoding='UTF-8') as file:
    json.dump(data["data"][0]["quote"]["USD"], file, indent=4)"""
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

"""with open('price_file.json', 'r', encoding='UTF-8') as file:
  data = json.load(file)"""

"""data_values = np.array(list(data.values())[:-1]).reshape(1, -1)""" #преобразуем словарь в список и исключаем последний элемент

data_values = np.array(list(data["data"][0]["quote"]["USD"].values())[:-13]).reshape(1, -1)


print(data_values)

