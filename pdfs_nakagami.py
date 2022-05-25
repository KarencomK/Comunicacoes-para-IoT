##pdfs da distribuição de nakagami

import numpy as np
from scipy.stats import nakagami
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

#Calcule os quatro primeiros momentos:
nu = 4.97
mean, var, skew, kurt = nakagami.stats(nu, moments='mvsk')

#Exiba a função de densidade de probabilidade ( pdf):
x = np.linspace(nakagami.ppf(0.01, nu),
                nakagami.ppf(0.99, nu), 100)
ax.plot(x, nakagami.pdf(x, nu),
       'r-', lw=5, alpha=0.6, label='nakagami pdf')

#Alternativamente, o objeto de distribuição pode ser chamado (como uma função) para fixar os parâmetros de forma, localização e escala. Isso retorna um objeto RV “congelado” mantendo os parâmetros fornecidos fixos.
#Congele a distribuição e exiba os congelados pdf:
rv = nakagami(nu)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

#Verifique a precisão de cdf e ppf:
vals = nakagami.ppf([0.001, 0.5, 0.999], nu)
np.allclose([0.001, 0.5, 0.999], nakagami.cdf(vals, nu))
True

#Gerar números aleatórios:
r = nakagami.rvs(nu, size=1000)

#E compare o histograma:
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()