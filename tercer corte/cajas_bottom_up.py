import random
import time

from matplotlib import pyplot as plt

def max_height_bottom_up(boxes):

    rotations = [] #C1 1

    for height, width, length in boxes: #C2 n
        rotations.append((height,width,length)) #C3 n-1
        rotations.append((width,height,length)) #C4 n-1
        rotations.append((length,width,height)) #C5 n-1

    rotations.sort(key=lambda x: x[1] * x[2], reverse=True) #C6 O(n log n) debido a que python usa timsort cuya complejidad es la mencionada

    n = len(rotations) #C7 1

    # max_height[i] = altura máxima con i como base
    max_height = [0] * n #C8 1

    for i in range(n): #C9 n
        max_height[i] = rotations[i][0] #C10 n-1

    for i in range(1,n): #C11 n
        for j in range(i): #C12 n^2
            if (rotations[i][1] < rotations[j][1] and
                rotations[i][2] < rotations[j][2]): #C13 n^2

                max_height[i] = max(max_height[i], max_height[j] + rotations[i][0]) #C14 n^2

    return max(max_height) #C15 1
        
#Complejidad total O(n^2)

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
    max_height_bottom_up(boxes)
    end = time.perf_counter()
    
    real_times.append(end - start)


theoretical_times = [n**2 for n in n_values]
scale_factor = real_times[-1] / theoretical_times[-1]
theoretical_times = [t * scale_factor for t in theoretical_times]


plt.figure(figsize=(10, 6))
plt.plot(n_values, real_times, 'bo-', label='Tiempo real bottom up')
plt.plot(n_values, theoretical_times, 'r--', label='Tiempo teórico O(n²)')
plt.xlabel('Número de cajas')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación entre tiempo real y teórico O(n²)')
plt.legend()
plt.grid(True)
plt.show()
boxes = [(4, 6, 7), (1, 2, 3), (4, 5, 6), (10, 12, 32)]

print('Altura máxima: ', max_height_bottom_up(boxes))
    

    