import random
import time
from matplotlib import pyplot as plt
from memo_cut_rod_ext import extended_memo_cut_rod
from bottom_up_ext import extended_bottom_up
from cut_rod import cut_rod

n = list(range(0, 800, 5))
p = []
cut_rod_times = []
bottom_up_times = []
memo_times = []

for size in n:
    len_p = len(p)
    if len_p == 0:
        p.append(random.randint(1, 5))
        len_p = 1

    for i in range(len_p, size):
        p.append(p[-1] + random.randint(1, 10))

    if size <= 25:
        start_time = time.perf_counter()
        cut_rod(p, size)
        end_time = time.perf_counter()
        cut_rod_times.append(end_time - start_time)
    else:
        cut_rod_times.append(None)

    start_time = time.perf_counter()
    extended_memo_cut_rod(p, size)
    end_time = time.perf_counter()
    memo_times.append(end_time - start_time)

    start_time = time.perf_counter()
    extended_bottom_up(p, size)
    end_time = time.perf_counter()
    bottom_up_times.append(end_time - start_time)

# Filtrar datos válidos para cut_rod
n_cut_rod = [x for x, y in zip(n, cut_rod_times) if y is not None]
cut_rod_filtered = [y for y in cut_rod_times if y is not None]

plt.figure(figsize=(8, 6))
plt.plot(n_cut_rod, cut_rod_filtered, marker='o', linestyle='-', color='black', linewidth=1.5,
         markersize=4, label='cut_rod (recursivo)')
plt.plot(n, memo_times, marker='s', linestyle='--', color='blue', linewidth=1.5,
         markersize=4, label='memoized')
plt.plot(n, bottom_up_times, marker='^', linestyle='-.', color='green', linewidth=1.5,
         markersize=4, label='bottom up')

plt.xlabel('Longitud de la varilla (n)', fontsize=12)
plt.ylabel('Tiempo de ejecución (s)', fontsize=12)
plt.title('Comparación de algoritmos de corte de varilla', fontsize=14)
plt.legend(loc='upper left', fontsize=10, frameon=True, facecolor='white')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
