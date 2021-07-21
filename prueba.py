import pandas_datareader.data as wb
import matplotlib.pyplot as plt

data = wb.DataReader(['PAYEMS','UNRATE'],'fred','2015-1-1')
data.to_excel("PAYEMS_UNRATE.xlsx")
print(data)