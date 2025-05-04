def memoized_cut_rod(p,n):
    r = [float('-inf')] * n
    return memoized_cut_rod_aux(p,n,r)

def memoized_cut_rod_aux(p,n,r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n+1):
            q = max(q, p[i-1] + memoized_cut_rod_aux(p, n-i, r))
    r[n] = q
    return q


n = 7
p = [1,5,8,9,10,17,17,20,24,30]
print(memoized_cut_rod(p,n))