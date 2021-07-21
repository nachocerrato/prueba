import pandas as pd
import numpy as np
from pandas_datareader import data as wb

assets = ['MSFT','UNP','GOOG','IBM']
data = wb.DataReader(assets,data_source='yahoo', start='2020-1-1')['Adj Close']
returns = data.pct_change()[1:]

#print(returns)
#print(returns.head())
#print(returns.tail())
#print(returns.dropna())
#print(returns.reset_index())
#print(returns.fillna(0))
#print(returns.fillna({'MSFT':0,'UNP':3}))
#print(returns.describe())
#print(returns[['MSFT', 'UNP']])
#print(returns.iloc[0])
#print((data[(data['MSFT'] > 250) & (data['GOOG'] > 1800)]))

log_returns = np.log(1 + data.pct_change()[1:])
log_returns.mean()
log_returns.var()
log_returns.std()
log_returns.cov()
log_returns.corr()