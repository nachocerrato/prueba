import numpy as np
import pandas_datareader.data as wb
import matplotlib.pyplot as plt

ticker = ['FB']
data = wb.DataReader(ticker, 'yahoo', '2021-3-1')

period = 5
data['MA'] = data['Close'].rolling(period).mean()
data['EWM'] = data['Close'].ewm(span=period, min_periods=period).mean()
data = data[['Close', 'MA', 'EWM']].iloc[period:]

plt.plot(data.index, data)
plt.title("Ejemplo de medias")
plt.ylabel("Precio y medias de " + str(ticker))
plt.legend(data[['Close', 'MA', 'EWM']])
plt.show()
