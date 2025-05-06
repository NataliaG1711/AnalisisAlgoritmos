import random
import time

from matplotlib import pyplot as plt


def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n + 1):
        m[i][i] = 0

    for l in range(2, n + 1):  # Longitud de la cadena
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")



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


plt.figure(figsize=(8, 6))
plt.plot(n, times, marker='o', linestyle='-', color='k')
plt.xlabel(' Número de matrices (n)')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución Matrix chain order')
plt.grid()
plt.show()

