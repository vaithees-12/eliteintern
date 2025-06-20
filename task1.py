import requests
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: API call to CoinGecko to get top 10 cryptocurrencies
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False
}

response = requests.get(url, params=params)
data = response.json()

# Step 2: Extract names and prices
coin_names = [coin["name"] for coin in data]
coin_prices = [coin["current_price"] for coin in data]

# Step 3: Create a DataFrame
df = pd.DataFrame({
    "Cryptocurrency": coin_names,
    "Price (USD)": coin_prices
})

# Step 4: Plot bar chart
plt.figure(figsize=(10, 6))
plt.bar(df["Cryptocurrency"], df["Price (USD)"], color='green')
plt.title("Top 10 Cryptocurrency Prices")
plt.xlabel("Cryptocurrency")
plt.ylabel("Price in USD")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
