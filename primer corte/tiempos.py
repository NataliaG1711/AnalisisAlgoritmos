import math

def max_n_factorial(t):
    n = 1
    while math.factorial(n) <= t:
        n += 1
    return n - 1

t = 3.1536*(10**15) 
print(max_n_factorial(t))
