# Com a ajuda do método numpy.random.rayleigh() ,
# podemos obter as amostras aleatórias da distribuição Rayleigh e retornar as amostras aleatórias.

#https://www.geeksforgeeks.org/numpy-random-rayleigh-in-python/
import numpy as np
import matplotlib.pyplot as plt

# Using rayleigh() method
gfg = np.random.rayleigh(3.4, 50000)

plt.figure()
plt.hist(gfg, bins = 50, density = True)
plt.show()
