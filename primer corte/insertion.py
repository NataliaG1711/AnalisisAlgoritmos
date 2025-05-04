def insertion_desc(l):
    for i in range(1, len(l)+1):
        k=i-1
        while (k>0) and (l[k]<l[k-1]):
            l[k], l[k-1] = l[k-1], l[k]
            k -= 1
        print(l)

listaimpares = [5,87,3,0,56]
#insertion_desc(listaimpares)

def insertion_sort(A):
    for j in range(1, len(A)):
        k = A[j]
        i = j-1
        while i >= 0 and A[i] > k:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = k
        print(A)

insertion_sort(listaimpares)

def insertion_sort_desc(A):
    for j in range(1, len(A)):
        k = A[j]
        i = j-1
        while i >= 0 and A[i] < k:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = k
        print(A)

#insertion_sort_desc(listaimpares)