#scipy.stats.rice() é uma variável aleatória contínua de Rice. 
# Ele é herdado dos métodos genéricos como uma instância da classe rv_continuous . 
# Ele completa os métodos com detalhes específicos para essa distribuição específica.

#https://www.geeksforgeeks.org/python-rice-distribution-in-statistics/?ref=gcse
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rice

numargs = rice.numargs
a, b = 4.32, 3.18
rv = rice (a, b)

print ("RV : \n", rv)

quantile = np.arange (0.01, 1, 0.1) 
# Random Variates 
R = rice.rvs(a, b) 
print ("Random Variates : \n", R) 

# PDF 
R = rice.pdf(a, b, quantile) 
print ("\nProbability Distribution : \n", R) 

distributionn = np.linspace(0, np.minimum(rv.dist.b, 1)) 
print("Distribution : \n", distributionn) 
plot = plt.plot(distributionn, rv.pdf(distributionn))

plt.show()