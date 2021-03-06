#Ejercicio4
# 'y' es una senal en funcion del tiempo 't' con las unidades descritas en el codigo.
# a. Grafique la senal en funcion del tiempo en la figura 'senal.png' ('y' vs. 't')
# b. Calule la transformada de Fourier (sin utilizar funciones de fast fourier transform) y
# grafique la norma de la transformada en funcion de la frecuencia (figura 'fourier.png')
# c. Lleve a cero los coeficientes de Fourier con frecuencias mayores que 10000 Hz y calcule 
# la transformada inversa para graficar la nueva senal (figura 'filtro.png')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



n = 512 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 128 ) #128 samples per frequency
t = np.linspace( 0, (n-1)*dt, n) 
y = np.sin(2 * np.pi * f * t) + np.cos(2 * np.pi * f * t * t)
noise = 1.4*(np.random.rand(n)+0.7)
y  =  y + noise

plt.plot(y, t)
plt.xlabel("Senal")
plt.ylabel("Tiempo")
plt.title("Senal vs Tiempo")
plt.savefig("senal.png")
plt.show()

#Transformada de fourier
yfourier=[]
def fourier():
    for i in range(n):
        yf = 0.0
        for j in range(n):
            yf += y[i] * np.exp(-1j * 2*num.pi* i*j/N)
        yfourier.append(yf / n)
        if(yfourier[i] == 10000):
            yfourier[i] == 0
            
    return yfourier

    


















