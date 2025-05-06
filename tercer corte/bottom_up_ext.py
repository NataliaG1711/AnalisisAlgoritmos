import random
import time

from matplotlib import pyplot as plt

def extended_bottom_up(p, n):
    r = [0] * (n + 1)
    s = [0] * (n + 1)

    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            if i <= len(p):
                if q < p[i - 1] + r[j - i]:
                    q = p[i - 1] + r[j - i]
                    s[j] = i  #Se almacena el corte optimo
        r[j] = q

    return r[n], s  # r[n] = valor máximo, s = lista de cortes

def print_cut_rod_solution(p, n):
    r, s = extended_bottom_up(p, n)
    result = []
    while n > 0:
        result.append(s[n])  # s[n] = corte óptimo
        n -= s[n]  # reducir longitud varilla
    return result

'''

n = list(range(0, 1001, 5))
#n = [1,5,7,10,1100]
p = []
times = []

for size in n:
    len_p = len(p)
    if len_p == 0:
        p.append(random.randint(1, 5))
        len_p = 1

    for i in range(len_p, size):
        p.append(p[-1] + random.randint(1, 10))

    #print(p)

    start_time = time.perf_counter()
    extended_bottom_up(p, size)
    end_time = time.perf_counter()  
    times.append(end_time - start_time)

#print("Valor máximo:", valor)
#print("Cortes óptimos:", print_cut_rod_solution(p, n))

plt.figure(figsize=(8, 6))
plt.plot(n, times, marker='o', linestyle='-', color='k')
plt.xlabel('Número de puntos (n)')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución en función de n')
plt.grid()
plt.show()
'''
