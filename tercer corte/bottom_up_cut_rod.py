def bottom_up_cut_rod(p,n):

    r = [0] * n 

    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            q = max(q, p[i - 1] + r[j - i])
        r[j] = q
    return r[n]

n= 7
p = [1,5,8,9,10,17,17,20,24,30]
print(bottom_up_cut_rod(p,n))