def cut_rod(p,n):
    if n == 0:
        return 0
    else:
        q = float('-inf')
        for i in range (1, n+1):
            q = max(q, p[i-1] + cut_rod(p, n-i))
        return q
    
n = 7
p = [1,5,8,9,10,17,17,20,24,30]
print(cut_rod(p,n))