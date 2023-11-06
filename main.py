# Import necessary libraries
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os
import numpy as np
import pandas as pd

# Set the start date to January 1, 2010
start_date = "2010-01-01"

# Calculate the date of the day before yesterday
end_date = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')

# Download historical data for WIG-20 and S&P 500 using yfinance
wig20 = yf.download('^WIG20', start=start_date, end=end_date)['Adj Close']
sp500 = yf.download('^GSPC', start=start_date, end=end_date)['Adj Close']

# Calculate daily returns for both indices
wig20_returns = wig20.pct_change().dropna()
sp500_returns = sp500.pct_change().dropna()

# Calculate the correlation coefficient
correlation = wig20_returns.corr(sp500_returns)

# Define the directory path for saving visualizations
visualization_dir = "visualizations"

# Create the directory if it doesn't exist
if not os.path.exists(visualization_dir):
    os.makedirs(visualization_dir)

# Plot daily returns of WIG-20 and S&P 500
plt.figure(figsize=(12, 6))
plt.plot(wig20_returns.index, wig20_returns, label='WIG-20', color='blue')
plt.plot(sp500_returns.index, sp500_returns, label='S&P 500', color='black')
plt.title("Daily Returns of WIG-20 and S&P 500")
plt.xlabel("Date")
plt.ylabel("Daily Returns")
plt.legend()

# Annotate the plot with the correlation
plt.annotate(f"Correlation: {correlation:.2f}", xy=(0.05, 0.9), xycoords='axes fraction', fontsize=12, color='red')

plt.grid()
plt.savefig(os.path.join(visualization_dir, "daily_returns_plot.png"))
plt.show()