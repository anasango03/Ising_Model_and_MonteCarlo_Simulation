import math
import numpy as np
import random
import numba
from numba import set_num_threads
import matplotlib.pyplot as plt

set_num_threads(4)




# Definimos los parámetros
N = 32  # Tamaño de la matriz
S = 2*np.random.randint(2, size=(N,N))-1  # Rellenamos la matriz con 1 y -1 de forma aleatoria.
l = 10**4  # Número de iteraciones
T = np.linspace(1.5, 3.5, 10) #Vector de temperaturas
mag_media=np.zeros(10)




for t in range(10):    
    M=0
    for k in range(l): 
        for i in range(N):
            for j in range(N):
                m = np.random.randint(0, N)
                n = np.random.randint(0, N)
                p=S[m,n]
    
                AE = 2*S[m,n]*(S[(m+1)%N,n] + S[m,(n+1)%N] + S[(m-1)%N,n] + S[m,(n-1)%N])
            
                if AE < 0:
                    p *= -1
                elif random.random() < np.exp(-AE/T[t]):
                    p *= -1
                S[m,n] = p
                    
            
                        
        Mag = np.sum(S)
        M = M+Mag

    mag_media[t]= M/(l*N**2)


#Graficamos los resultados
plt.figure(figsize=(7, 7), layout = 'tight')
plt.plot(T, abs(mag_media), label = 'Magnetización media') 
plt.scatter(T, abs(mag_media), label = 'Magnetización media') 
plt.xlabel('Temperatura') 
plt.ylabel('Magnetización')                                   

plt.show()

