import random
import time

from matplotlib import pyplot as plt
import numpy as np


def extended_memo_cut_rod(p, n):
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for i in range(n + 1):
        r[i] = float('-inf')
    q = memo_cut_rod_aux(p, n, r, s)
    return q, solution(s, n)

def memo_cut_rod_aux(p, n, r, s):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n + 1):
            temp = p[i - 1] + memo_cut_rod_aux(p, n - i, r, s)
            if q < temp:
                q = temp
                s[n] = i 
    r[n] = q
    return q

def solution(s, n):
    result = []
    while n > 0:
        result.append(s[n])
        n -= s[n]
    return result


n = 7
p = [1,5,8,9,10,17,17,20,24,30]
valor, cortes = extended_memo_cut_rod(p,n)
print("Valor máximo:", valor)
print("Cortes óptimos:", cortes)


n = list(range(0, 800, 10))
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
    extended_memo_cut_rod(p, size)
    end_time = time.perf_counter()  
    times.append(end_time - start_time)

n2 = np.array(n)
cubic = (n2**2) / (n2[-1] ** 2) * max(times)

plt.figure(figsize=(8, 6))
plt.plot(n, times, marker='o', linestyle='-', color='k', label='Memoized cut rod')
plt.plot(n2,cubic,marker='o', linestyle='-', color='purple', label='n^2')
plt.xlabel('Longitud de la varilla (n)')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución Memoized cut rod')
plt.legend()
plt.grid()
plt.show()
