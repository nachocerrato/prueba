from random import seed, randrange, randint
import random
import matplotlib.pyplot as plt

seed(1)
random_walk = list()
random_walk.append(-1 if random() < 0.5 else 1)
for i in range (1,100):
    movimiento = -1 if random() < 0.5 else 1
    valor = random_walk[i-1] + movimiento
    random_walk.append(valor)
plt.plot(random_walk)
plt.show()