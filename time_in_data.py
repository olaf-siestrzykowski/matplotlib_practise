import pandas as pd
import yfinance as yf
from IPython.core.pylabtools import figsize
from matplotlib import pyplot as plt

df = yf.download('AAPL', start='2022-01-01', end='2023-01-01')

df.index = pd.to_datetime(df.index)

jan = pd.to_datetime('2022, 1, 1')
print(jan.day_name())

march = df.loc['2022-03']

plt.figure(figsize=(15, 5))
plt.title("Stock Prices 2022")
plt.xlabel('Month')
plt.ylabel('Price')
plt.plot(df['Adj Close'])
plt.show()

df2 = pd.read_csv('Data Manipulation in Python Master Python, Numpy & Pandas/ETH_1h.csv')

df2.set_index('Date', inplace=True)
df2.index = pd.to_datetime(df2.index, format='%Y-%m-%d %I-%p')

print(march)
