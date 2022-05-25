#pdfs da distribuição de rayleigh

from scipy.stats import rayleigh
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(1, 1)

#Calcule os quatro primeiros momentos:
mean, var, skew, kurt = rayleigh.stats(moments='mvsk')

#Exiba a função de densidade de probabilidade ( pdf):
x = np.linspace(rayleigh.ppf(0.01),
                rayleigh.ppf(0.99), 100)
ax.plot(x, rayleigh.pdf(x),
       'r-', lw=5, alpha=0.6, label='rayleigh pdf')

#Alternativamente, o objeto de distribuição pode ser chamado (como uma função) para fixar os parâmetros de forma, localização e escala. Isso retorna um objeto RV “congelado” mantendo os parâmetros fornecidos fixos.
#Congele a distribuição e exiba os congelados pdf:
rv = rayleigh()
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

#Verifique a precisão de cdf e ppf:
vals = rayleigh.ppf([0.001, 0.5, 0.999])
np.allclose([0.001, 0.5, 0.999], rayleigh.cdf(vals))

#Gerar números aleatórios:
r = rayleigh.rvs(size=1000)

#E compare o histograma:
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()