import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Crypto Price Dashboard", layout="wide")

st.title("🚀 Crypto Price Dashboard")

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin,ethereum,solana,dogecoin",
    "vs_currencies": "inr",
    "include_24hr_change": "true"
}

try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if "bitcoin" not in data:
        st.error("CoinGecko API returned an unexpected response.")
        st.write(data)
        st.stop()

    btc = data["bitcoin"]["inr"]
    eth = data["ethereum"]["inr"]
    sol = data["solana"]["inr"]
    doge = data["dogecoin"]["inr"]

    btc_change = data["bitcoin"].get("inr_24h_change", 0)
    eth_change = data["ethereum"].get("inr_24h_change", 0)
    sol_change = data["solana"].get("inr_24h_change", 0)
    doge_change = data["dogecoin"].get("inr_24h_change", 0)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("₿ Bitcoin", f"₹{btc:,.0f}", f"{btc_change:.2f}%")

    with col2:
        st.metric("Ξ Ethereum", f"₹{eth:,.0f}", f"{eth_change:.2f}%")

    col3, col4 = st.columns(2)

    with col3:
        st.metric("◎ Solana", f"₹{sol:,.0f}", f"{sol_change:.2f}%")

    with col4:
        st.metric("🐕 Dogecoin", f"₹{doge:,.2f}", f"{doge_change:.2f}%")

    st.divider()
    st.write(
        f"Last Updated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    )

except requests.exceptions.RequestException as e:
    st.error(f"API Request Failed: {e}")

except Exception as e:
    st.error(f"Unexpected Error: {e}")