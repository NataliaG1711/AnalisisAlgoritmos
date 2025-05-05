def memo_cut_rod(p,n):
  r=[-1]*n
  for i in range(0,n):
    r[i]=float('-inf')
  return memo_cut_rod_aux(p,n,r)

def memo_cut_rod_aux(p,n,r):
  if r[n-1]>=0:
    return r[n-1]
  if n==0:
    q=0
  else:
    q=float('-inf')
    for i in range(1,n+1):
      q = max(q,p[i-1]+memo_cut_rod_aux(p,n-i,r))
  r[n-1]=q
  return q

n = 7
p = [1,5,8,9,10,17,17,20,24,30]
print(memo_cut_rod(p,n))