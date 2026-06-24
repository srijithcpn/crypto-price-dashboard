import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Crypto Price Dashboard", layout="wide")

st.title("🚀 Crypto Price Dashboard")

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
"ids": "bitcoin,ethereum,solana,dogecoin",
"vs_currencies": "inr"
}

response = requests.get(url, params=params, timeout=10)

if response.status_code != 200:
st.error(f"API Error: {response.status_code}")
st.stop()

data = response.json()

if "bitcoin" not in data:
st.error("Unexpected API response")
st.write(data)
st.stop()

btc = data["bitcoin"]["inr"]
eth = data["ethereum"]["inr"]
sol = data["solana"]["inr"]
doge = data["dogecoin"]["inr"]

col1, col2 = st.columns(2)

with col1:
st.metric("₿ Bitcoin", f"₹{btc:,.0f}")

with col2:
st.metric("Ξ Ethereum", f"₹{eth:,.0f}")

col3, col4 = st.columns(2)

with col3:
st.metric("◎ Solana", f"₹{sol:,.2f}")

with col4:
st.metric("🐕 Dogecoin", f"₹{doge:,.2f}")

st.divider()

st.write(
f"Last Updated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)
