def extended_memo_cut_rod(p, n):
    r = [-1] * (n + 1)
    s = [0] * (n + 1)
    for i in range(n + 1):
        r[i] = float('-inf')
    q = memo_cut_rod_aux(p, n, r, s)
    return q, solution(s, n)

def memo_cut_rod_aux(p, n, r, s):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n + 1):
            temp = p[i - 1] + memo_cut_rod_aux(p, n - i, r, s)
            if q < temp:
                q = temp
                s[n] = i 
    r[n] = q
    return q

def solution(s, n):
    result = []
    while n > 0:
        result.append(s[n])
        n -= s[n]
    return result

n = 7
p = [1,5,8,9,10,17,17,20,24,30]

valor, cortes = extended_memo_cut_rod(p, n)
print("Valor máximo:", valor)
print("Cortes óptimos:", cortes)