import pandas_datareader.data as wb
import matplotlib.pyplot as plt

data = wb.DataReader('AAPL', 'yahoo', '2018')

period = 30
data['std'] = data['Close'].rolling(period).std()
data['MA'] = data['Close'].rolling(period).mean()

data['BUP'] = data['MA'] + 2*data['std']
data['BDW'] = data['MA'] + 2*data['std']
data = data.iloc[period:]

plt.plot(data.index, data[['Close', 'MA', 'BUP', 'BDW']])
plt.legend(data[['Close','MA', 'BUP', 'BDW']])
plt.show()