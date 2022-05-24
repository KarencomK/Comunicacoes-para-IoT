#Suponha o seguinte conjunto de medidas, onde d0 = 1 m, Pt = 2 mW e fc = 1.8 GHz. Estime um modelo de perda de propagação do tipo log-normal, assumindo espaço-livre para determinar P r(d0).

import numpy as np
import matplotlib.pyplot as plt
import math


#Variable declaration
Prd0 = 2*10**6; #potencia recebida
d0= 10**3; #distancia de referencia 1km
d= np.linspace(10, 200, num= 20); #distância em m

#Calculations

Pr_d0= Prd0 * (d0/d)**2; ##free space

#MSE
y = d
y_bar = Pr_d0
summation = 0  #variable to store the summation of differences
n = len(y) #finding total number of items in list
for i in range (0,n):  #looping through each element of the list
  difference = y[i] - y_bar[i]  #finding the difference between observed and predicted value
  squared_difference = difference**2  #taking square of the differene 
  summation = summation + squared_difference  #taking a sum of all the differences
MSE = summation/n  #dividing summation by total values to obtain average
print ("O erro quadrado médio é: ")
print(MSE);


Pl_d = Pr_d0 + MSE * np.log10(d/d0)


plt.figure()
plt.xscale('log')
#plt.yscale('log')
#plt.scatter(Pr_FS,  Pr_LD1, color='purple')
plt.title('Path loss model of the type log-normal Plot')
plt.plot(d, Pl_d, label ='Free space')
plt.xlabel('Distância (KM)')
plt.ylabel('P_r')
plt.legend(loc=2, frameon=False, fontsize='medium')
plt.show()

