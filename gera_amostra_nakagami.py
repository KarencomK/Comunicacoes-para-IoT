#scipy.stats.nakagami() é uma variável aleatória contínua Nakagami.
# Ele é herdado dos métodos genéricos como uma instância da classe rv_continuous
# Ele completa os métodos com detalhes específicos para essa distribuição específica.

#https://www.geeksforgeeks.org/python-nakagami-distribution-in-statistics/

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nakagami

numargs = nakagami.numargs 
a, b = 4.32, 3.18
rv = nakagami(a, b) 

print ("RV : \n", rv) 

quantile = np.arange (0.01, 1, 0.1) 
  
# Random Variates 
R = nakagami.rvs(a, b) 
print ("Random Variates : \n", R) 
# PDF 
R = nakagami.pdf(a, b, quantile) 
print ("\nProbability Distribution : \n", R) 

distribution = np.linspace(0, np.minimum(rv.dist.b, 3)) 
print("Distribution : \n", distribution) 

plot = plt.plot(distribution, rv.pdf(distribution)) 
plt.show()
