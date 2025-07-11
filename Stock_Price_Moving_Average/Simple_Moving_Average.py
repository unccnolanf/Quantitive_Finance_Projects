import yfinance as yf
import matplotlib.pyplot as plt

# Download historical stock data from Yahoo Finance
# Change the ticker to any valid symbol (e.g., 'AAPL', 'TSLA', etc.)
ticker = 'AAPL'
data = yf.download(ticker, start='2023-01-01', end='2024-01-01')

# Simple Moving Average (20)
sma_window = 20
data['SMA20'] = data['Close'].rolling(window=sma_window).mean()

# Plot the closing price and the SMA on the same chart
plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label=f'{ticker} Close Price', linewidth=1.5)
plt.plot(data['SMA20'], label=f'{sma_window}-Day SMA', linewidth=1.5, color='orange')

# Add title and labels
plt.title(f'{ticker} Closing Price & {sma_window}-Day SMA')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
