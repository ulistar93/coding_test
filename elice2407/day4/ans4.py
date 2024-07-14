from collections import defaultdict
import pdb

v=defaultdict(list)
dp=[None]*100050
inf=int(1e12)

def dfs(x:int ,par:int):
    global dp,v
    
    ret=inf
    
    for nxt in v[x]:
        if nxt==par:
            continue
            
        dfs(nxt,x)
        ret=min(ret,dp[nxt])
        
    if ret==inf:
        ret=0
        
    dp[x]=x-ret
    print("dp[",x,"]=",dp[x])
    pdb.set_trace()

n=int(input())

for _ in range(1,n):
    a,b=(map(int,input().split()))
    v[a].append(b)
    v[b].append(a)

pdb.set_trace()
dfs(1, 0)

for i in range(1,n+1):
    print('1' if dp[i]>=0 else '0')