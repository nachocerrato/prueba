import pandas as pd
import numpy as np

tabla0 = pd.DataFrame(np.random.randint(0,9999, size=(2,3)),columns=['Número1', 'Número2', 'Número3'])
tabla1 = pd.DataFrame(np.random.randint(-10000,100, size=(2,2)),columns=['Número4', 'Número5'])
tabla2 = pd.DataFrame(np.random.rand(100))
tabla3 = pd.DataFrame(np.random.randn(2,5))
tabla4 = pd.DataFrame(np.random.uniform(-10000,5000, size=(100,2)))


data = pd.DataFrame()
data = pd.concat([tabla0,tabla1,tabla2,tabla3,tabla4], axis=1)
data.fillna('Hola')