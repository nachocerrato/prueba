from pandas_datareader import data as wb

data = wb.DataReader('TSLA','yahoo')
print(data)