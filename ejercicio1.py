# Ejercicio1
# A partir de los arrays x y fx calcule la segunda derivada de fx con respecto a x. 
# Esto lo debe hacer sin usar ciclos 'for' ni 'while'.
# Guarde esta segunda derivada en funcion de x en una grafica llamada 'segunda.png'

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = np.linspace(0,2.,10)
fx = np.array([0., 0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.])
d1x = fx
d2x = fx

for i in range(1, len(x)):
    d1x[i] = (fx[i]-fx[i-1])/(x[i]-x[i-1])
    d2x[i] = (d1x[i]-d1x[i-1])/(x[i]-x[i-1])
    
plt.plot(x, d2x)
plt.xlabel("Posicion")
plt.ylabel("Segunda derivada")
plt.title("Segunda derivada vs posicion")
plt.savefig("segunda.png")
plt.show()
    

    



