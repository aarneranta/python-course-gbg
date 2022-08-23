# -*- coding: utf-8 -*-
"""
Du ska köpa ett hus och vill göra linjär regression för att ta reda på ungefär
vad ett hus kostar beroende på hur stort det är. Du tittar på hemnet och tar 
fram följande data:
    x = [25, 40, 50, 55, 60, 70, 80] (yta)
    y = [1.5, 2, 2.2, 3.0, 2.9, 3.5 3.6] (pris i miljoner)

Börja med att plotta all data,
Linjen kommer ha formen y=kx+m, testa dig fram med olika värden på k och m 
för att hitta vilka värden som minimerar MSE
"""
import matplotlib.pyplot as plt
import numpy as np

x = [25, 40, 50, 55, 60, 70, 80]
y = [1.5, 2, 2.2, 3.0, 2.9, 3.5, 3.6]

plt.plot(x,y, "ro")
plt.show()


#Paramterar
k = 0.045
m = 0.2

#summeringsvariabel
s = 0

#Hur många element har vi?
N = len(x)


#Beräkna MSE
for i in range(N):
    y_predicted = k*x[i]+m
    error = (y[i]-y_predicted)**2
    s = s + error
    
MSE = s / N


#Plotta en linje med våra x och y:
x_plot = np.linspace(0, 80)
y_plot = k*x_plot+m

plt.plot(x_plot,y_plot)
plt.plot(x,y, "ro")
plt.show()
print("MSE: " + str(MSE))





# ##################
# #Gradient descent#
# ##################

#Omvandla till numpy objekt
x = np.array([25, 40, 50, 55, 60, 70, 80])
y = np.array([1.5, 2, 2.2, 3.0, 2.9, 3.5, 3.6])


#Parametrar
k=1
m=0
lr = 0.0001
iters = 100

for i in range(iters): 
    y_pred = k*x + m  
    D_k = (-2/N) * sum(x * (y - y_pred))  # Derivative wrt k
    D_m = (-2/N) * sum(y - y_pred)  # Derivative wrt k
    k = k - lr * D_k  # Update k
    m = m - lr * D_m  # Update c



x_plot = np.linspace(0, 80)
y_plot = k*x_plot+m

plt.plot(x_plot,y_plot)
plt.plot(x,y, "ro")
plt.show()


for i in range(N):
    y_predicted = k*x[i]+m
    error = (y[i]-y_predicted)**2
    s = s + error
    
MSE = s / N

print("k: " + str(k))
print("m: " + str(m))

print("MSE: " + str(MSE))

