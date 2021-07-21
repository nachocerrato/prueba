# 1- Genera el siguiente DataFrame: 4 columnas: Edad, Peso, Altura ,Género || 18-80 años / 50.0-100.0/ Altura: 1.40-2/ 0-1

import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

edad = pd.DataFrame(np.random.randint(18,80, size=(10,1)), columns=['Edad'])
peso = pd.DataFrame(np.random.randint(50.0,100.0, size=(10,1)),columns=['Peso'])
altura = pd.DataFrame(np.random.randint(140,201, size=(10,1)), columns=['Altura'])
genero = pd.DataFrame(np.random.randint(0,2, size=(10,1)), columns=['Género'])

persona = pd.concat([edad, peso, altura, genero], axis=1)
persona

# 2- Busca 2 datos macroeconómicos en la página de la FRED y dibújalos (mejor si son números parecidos) dibújalos en un gráfico con títulos y ejes.

from matplotlib import pyplot as plt

plt.close()
macro = wb.DataReader(['H8B1058NCBCMG','H8B1023NCBCMG'],'fred','1975-1-1')
grafico2 = macro.plot(ylabel='Annual Change %', xlabel='Date')
plt.title('Deposits and loans')
plt.show()

# 2- Muestra también los cambios entre periodos (entre meses, días, años... en función de tus datos escogidos)

macro_dif = macro.diff()
macro_dif.to_csv('grafico.csv')
macro_dif.to_excel('grafico.xlsx')

# 3- Calcula los retornos simples y logarítmicos de las FAANG, partiendo de Mayo de 2017 y finalizando en Abril de 2019, y calcula la media, desviación estándar, varianza, covarianza y coeficiente de correlación.

from pandas_datareader import data as wb

assets = ['AMZN','AAPL','FB','GOOG','MSFT']
data = wb.DataReader(assets,'yahoo', '2017-5-1','2019-4-1')

returns = data.pct_change()[1:]
log_returns = np.log(1 + data.pct_change()[1:])


print(returns.tail())
print(log_returns.head())
print(log_returns.mean())
print(log_returns.var())
print(log_returns.cov())
print(log_returns.corr())


# 3- A continuación dibuja con matplotlib el precio de cierre de Apple.


from matplotlib import pyplot as plt

cierre = wb.DataReader('AAPL','yahoo','2020-1-1')['Adj Close']
grafico = cierre.plot(ylabel='USD', xlabel='Fecha')
plt.show()

# 4- Trata de realizar la desmotración de la función pct_change() con los retornos del ejercicio 3 ((returns/returns(-1)-1) Puedes visualizar datos con la función head()

print(log_returns.head())
 
# 5- Instala la librería "seaborn" y trata de dibujar una matriz de correlación con el coeficiente de correlación del ej.2, puedes usar el módulo heatmap para ello. (Si tienes dudas puedes consultar la documentación).

import seaborn as sns

correlacion = log_returns.corr()
ax = sns.heatmap(correlacion, annot=True, cmap="YlGnBu", linewidths=.5)
plt.show()


# 6- Utiliza las funciones que vimos en el ejercicio retornos.py de la clase 4 y úsalas para el ejercicio 3, tanto para la variable data como para los retornos.



# 7- Define una función llamada tabla_del_7() que realice de forma automática la tabla de multiplicar del 7.