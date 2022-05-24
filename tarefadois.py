#Se a potência recebida a uma distância de referência de 1km for de 1μW, trace (em escala log-log) a potência do sinal recebido para distâncias de 1km a 20km para os seguintes modelos de perda de percurso:

import numpy as np
import matplotlib.pyplot as plt
import math

#Variable declaration
Prd0 = 10**-6; #potencia recebida
d0=1000; #distancia de referencia 10^3
d= np.linspace(1000, 20000, num= 100);#1000:100:20000; #distância em km que varia de 100 em 100

#Calculations

Pr_FS = Prd0 * (d0/d)**2; #free space
Pr_LD1 = Prd0 * (d0/d)**3; #n=3
Pr_LD2 = Prd0 * (d0/d)**4; #n=4
Pr_Hata = Prd0 * (d0/d)**3.4; #hata

plt.figure()
plt.xscale('log')
plt.yscale('log')
#plt.scatter(Pr_FS,  Pr_LD1, color='purple')
plt.title('Log-Log Plot')
plt.plot(d, Pr_FS, label ='Free space')
plt.plot(d, Pr_LD1, label ='Log - Distant n = 3')
plt.plot(d, Pr_LD2, label ='Log - Distant n = 4')
plt.plot(d, Pr_Hata, label ='Hata')
plt.xlabel('Distância (KM)')
plt.ylabel('P_r')
plt.legend(loc=2, frameon=False, fontsize='medium')
plt.show()