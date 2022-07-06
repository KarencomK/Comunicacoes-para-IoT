##pdfs da distribuição de Rice

import numpy as np
from scipy.stats import rice
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

#Calcule os quatro primeiros momentos:
b = 0.775
mean, var, skew, kurt = rice.stats(b, moments='mvsk')

#Exiba a função de densidade de probabilidade ( pdf):
x = np.linspace(rice.ppf(0.01, b),
                rice.ppf(0.99, b), 100)
ax.plot(x, rice.pdf(x, b),
       'r-', lw=5, alpha=0.6, label='rice pdf')

#Alternativamente, o objeto de distribuição pode ser chamado (como uma função) para fixar os parâmetros de forma, localização e escala. Isso retorna um objeto RV “congelado” mantendo os parâmetros fornecidos fixos.
#Congele a distribuição e exiba os congelados pdf:
rv = rice(b)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

#Verifique a precisão de cdf e ppf:
vals = rice.ppf([0.001, 0.5, 0.999], b)
np.allclose([0.001, 0.5, 0.999], rice.cdf(vals, b))
True

r = rice.rvs(b, size=1000)

#E compare o histograma:
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()