import yfinance as yf   
import pandas as pd


# Downlaod Apple stock with ALL data
aapl = yf.Ticker("AAPL")

# Get historical data with actions (dividends and splits)
hist = aapl.history(start="2000-01-01", end="2017-12-31", actions=True)

# This will give you:
# - Date, Open, High, Low, Close, Volume
# - Dividends (Ex-Dividend column)
# - Stock Splits (Split Ratio column)

# Save to CSV
hist.to_csv("apple-stock-prices-from-20102017.csv")

print(hist.head())
print(hist.columns)