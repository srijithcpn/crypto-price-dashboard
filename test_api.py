import requests

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
   
    "ids": "ethereum",
    "vs_currencies": "inr"
}

response = requests.get(url, params=params)

data = response.json()


print("Ethereum Price:", data["ethereum"]["inr"])