import random
import time
from matplotlib import pyplot as plt
import numpy as np

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for i in range(n):
        m[i][i] = 0

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i+1}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

p = [1,2,3,4,5]
m, s = matrix_chain_order(p)
print('M:')
print(np.array(m))
print('S:')
print(np.array(s))

n = len(p) - 1
print_optimal_parens(s, 1, n-1)


n = list(range(0, 101, 2))
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
    matrix_chain_order(p)
    end_time = time.perf_counter()  
    times.append(end_time - start_time)

n2 = np.array(n)
cubic = (n2**3) / (n2[-1] ** 3) * max(times)

plt.figure(figsize=(8, 6))
plt.plot(n, times, marker='o', linestyle='-', color='k', label='matrix chain order')
plt.plot(n,cubic,marker='o',color='purple', label= 'n^3')
plt.xlabel(' Número de matrices (n)')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución Matrix chain order vs tiempo teórico')
plt.grid()
plt.legend()
plt.show()
