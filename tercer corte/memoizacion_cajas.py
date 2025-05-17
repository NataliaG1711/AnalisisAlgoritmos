import random
import time

from matplotlib import pyplot as plt

def dfs(index, rotations, memo):
    if memo[index] != -1: #C1 1
        return memo[index] #C2 1
    
    #Se dice que la altura máxima es la caja actual
    max_h = rotations[index][0] #C3 1
    n = len(rotations) #C4 1
    
    for i in range(n): #c5 n
        if i == index: #C6 n-1
            continue #C7 n-2
        if (rotations[i][1] < rotations[index][1] and rotations[i][2] < rotations[index][2]): #C8 n-1
            max_h = max(max_h, rotations[index][0] + dfs(i, rotations, memo)) #Se hacen n llamadas recursivas y en cada llamada hace el bucle n  C9 n^2
    
    memo[index] = max_h #C10 1
    return max_h #C11 1

#Costo total funcion O(n^2)

def max_height_top_down(boxes):
    rotations = []  # C12 1
    for height, width, length in boxes: #C13 n
        rotations.append((height, width, length)) #C14 n-1
        rotations.append((width, height, length))#C15 n-1
        rotations.append((length, width, height)) #C16 n-1
    
    rotations.sort(key=lambda x: x[1] * x[2], reverse=True) #c17 O(n log n) debido a que python usa timsort cuya complejidad es la mencionada
    
    n = len(rotations) #c18 1
    memo = [-1] * n #c19 1
    max_height = 0 #c20 1

    for i in range(n): #c21 n
        max_height = max(max_height, dfs(i, rotations, memo)) #c22 n^2
    
    return max_height #c23 1

#Costo total función O(n)


n_values = list(range(10, 1001, 10))
real_times = []

for size in n_values:
    boxes = []
    for _ in range(size):
        h = random.randint(1, 100)
        w = random.randint(1, 100)
        l = random.randint(1, 100)
        boxes.append((h, w, l))
    

    start = time.perf_counter()
    max_height_top_down(boxes)
    end = time.perf_counter()
    
    real_times.append(end - start)


theoretical_times = [n**2 for n in n_values]
scale_factor = real_times[-1] / theoretical_times[-1]
theoretical_times = [t * scale_factor for t in theoretical_times]


plt.figure(figsize=(10, 6))
plt.plot(n_values, real_times, 'bo-', label='Tiempo real')
plt.plot(n_values, theoretical_times, 'r--', label='Tiempo teórico O(n²)')
plt.xlabel('Número de cajas')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación entre tiempo real y teórico O(n²)')
plt.legend()
plt.grid(True)
plt.show()

boxes = [(4, 6, 7), (1, 2, 3), (4, 5, 6), (10, 12, 32)]

print(max_height_top_down(boxes))