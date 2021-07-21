import pandas_datareader.data as wb

data = wb.DataReader('FB','yahoo','2018-1-1')
print(data)