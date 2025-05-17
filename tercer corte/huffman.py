import math
import random
import string
import time
from matplotlib import pyplot as plt


class Node:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def min_heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i
        
        # Encuentra el menor entre el nodo actual y sus hijos
        if left < len(self.heap) and self.heap[left].freq < self.heap[smallest].freq:
            smallest = left
        
        if right < len(self.heap) and self.heap[right].freq < self.heap[smallest].freq:
            smallest = right
        
        # Si uno de los hijos es más pequeño, hace el intercambio
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    def build_min_heap(self):
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.min_heapify(i)

    def extract_min(self):
        if len(self.heap) < 1:
            return None
        min_node = self.heap[0]
        
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap.pop()

        if len(self.heap) > 0:
            self.min_heapify(0)

        return min_node
    
    def insert(self, node):
        self.heap.append(node)
        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i].freq < self.heap[parent].freq:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break
    
def huffman(c):
    q = MinHeap()
    q.heap = c[:]  # Copiar lista original
    q.build_min_heap()

    while len(q.heap) > 1:
        x = q.extract_min()
        y = q.extract_min()
        z = Node(None, x.freq + y.freq)
        z.left = x
        z.right = y
        q.insert(z)

    return q.extract_min()



def print_huffman_codes(root, code=""):
    if root is None:
        return
    
    # Si es una hoja (tiene un valor), imprime su código
    if root.value is not None:
        print(f"{root.value}: {code}")
        return

    # izquierda con 0
    print_huffman_codes(root.left, code + "0")
    # derecha con 1
    print_huffman_codes(root.right, code + "1")


data = [Node('a', 45), Node('b', 13), Node('c', 12), Node('d', 16), Node('e', 9), Node('f', 5)]
root = huffman(data)
print_huffman_codes(root)

sizes = list(range(10, 1001, 10))
real_times = []
theoretical_times = []


for n in sizes:
    letters = random.choices(string.ascii_letters, k=n)
    frequencies = [random.randint(1, 100) for _ in range(n)]
    data = [Node(letters[i], frequencies[i]) for i in range(n)]


    start = time.perf_counter()
    root = huffman(data)
    end = time.perf_counter()
    execution_time = end - start
    real_times.append(execution_time)
    


scaling_factor = sum(real_times) / sum(n * math.log2(n) for n in sizes)
theoretical_times = [(n * math.log2(n)) * scaling_factor for n in sizes]


plt.figure(figsize=(12, 7))
plt.plot(sizes, real_times, label='Tiempo (Segundos)', marker='o', linewidth=2)
plt.plot(sizes, theoretical_times, label='O(n log n)', linestyle='--', linewidth=2)
plt.xlabel('n', fontsize=12)
plt.ylabel('Tiempo (Segundos)', fontsize=12)
plt.title('Huffman - Tiempo de ejecución real vs teorico', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
