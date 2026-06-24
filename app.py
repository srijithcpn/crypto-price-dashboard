import streamlit as st
import requests

st.title("Crypto Price Dashboard")

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin,ethereum,solana,dogecoin",
    "vs_currencies": "inr",
    "include_24hr_change": "true"
}

response = requests.get(url, params=params)

data = response.json()
# Extract prices
btc = data["bitcoin"]["inr"]
eth = data["ethereum"]["inr"]
sol = data["solana"]["inr"]
doge = data["dogecoin"]["inr"]

# Extract changes
btc_change = data["bitcoin"]["inr_24h_change"]
eth_change = data["ethereum"]["inr_24h_change"]
sol_change = data["solana"]["inr_24h_change"]
doge_change = data["dogecoin"]["inr_24h_change"]

# Display prices
col1, col2 = st.columns(2)

with col1:
    st.metric("₿ Bitcoin", f"₹{btc:,}", f"{btc_change:.2f}%")

with col2:
    st.metric("Ξ Ethereum", f"₹{eth:,}", f"{eth_change:.2f}%")

col3, col4 = st.columns(2)

with col3:
    st.metric("◎ Solana", f"₹{sol:,}", f"{sol_change:.2f}%")

with col4:
    st.metric("🐕 Dogecoin", f"₹{doge:,}", f"{doge_change:.2f}%")

from datetime import datetime

st.write(f"Last Updated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
