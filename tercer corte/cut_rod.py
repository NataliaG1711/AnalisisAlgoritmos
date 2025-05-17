import random
import time

from matplotlib import pyplot as plt
import numpy as np


def cut_rod(p,n):
    if n == 0:
        return 0
    else:
        q = float('-inf')
        for i in range (1, n+1):
            q = max(q, p[i-1] + cut_rod(p, n-i))
        return q

n = 7
p = [1,5,8,9,10,17,17,20,24,30]
print(cut_rod(p,n))


n = list(range(0, 25, 2))
#n = [1,5,7,10]
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
    cut_rod(p, size)
    end_time = time.perf_counter()  
    times.append(end_time - start_time)

n2 = np.array(n)
expo = (2**n2) / (2**n2[-1]) * max(times)

plt.figure(figsize=(8, 6))
plt.plot(n, times, marker='o', linestyle='-', color='k', label='cut rod (recursive)')
plt.plot(n2, expo, marker='o', linestyle='-', color='purple', label='2^n')
plt.xlabel('Longitud de la varilla (n)')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución Cut rod')
plt.legend()
plt.grid()
plt.show()
