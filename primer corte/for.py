import time
from matplotlib import pyplot as plt
import numpy as np

def multiplicacion():
    tamaños = range(100, 10001, 1) 
    tiempos = []
    
    for n in tamaños:
        l = list(np.random.randint(100, size=n))
        tiempo_1 = time.perf_counter()
        for i in range(0, len(l)):    
            i *= 2
        tiempo_2 = time.perf_counter()
        tiempos.append(tiempo_2 - tiempo_1)
    
    #plt.plot(tamaños, tiempos)

    #plt.show()

    return tamaños, tiempos

#multiplicacion()


def division():
    tamaños = range(100, 10001, 1) 
    tiempos = []
    
    for n in tamaños:
        l = list(np.random.randint(100, size=n))
        tiempo_1 = time.perf_counter()
        for i in range(0, len(l)):    
            i /= 2
        tiempo_2 = time.perf_counter()
        tiempos.append(tiempo_2 - tiempo_1)
    
    #plt.plot(tamaños, tiempos)

    #plt.show()


#division()

    

def suma():
    tamaños = range(100, 10001, 1) 
    tiempos = []
    
    for n in tamaños:
        l = list(np.random.randint(100, size=n))
        tiempo_1 = time.perf_counter()
        for i in range(0, len(l)):    
            i += 2
        tiempo_2 = time.perf_counter()
        tiempos.append(tiempo_2 - tiempo_1)
    
    #plt.plot(tamaños, tiempos)

    #plt.show()
    
    return tamaños, tiempos

#suma()

def exponencial():
    exponentes = range(2,18)
    tiempos = []
    tamaños = []
    for exp in exponentes:
        n = 2**exp
        tamaños.append(n)
        l = list(np.random.randint(100, size=n))
        tiempo_1 = time.perf_counter()
        for i in range(0, len(l)):    
           pass 
        tiempo_2 = time.perf_counter()
        tiempos.append(tiempo_2 - tiempo_1)

    return tamaños, tiempos
    
    #plt.plot(tamaños, tiempos)

    #plt.show()


tamaños_suma, tiempos_suma = suma()

tamaños_multiplicacion, tiempos_multiplicacion = multiplicacion()

tamaños_exponencial, tiempos_exponencial = exponencial()

plt.plot(tamaños_suma, tiempos_suma, 'b-', label='Suma')
plt.plot(tamaños_multiplicacion, tiempos_multiplicacion, 'r-', label='Multiplicación')
plt.plot(tamaños_exponencial, tiempos_exponencial, 'k', label= 'Exponencial')
plt.show()