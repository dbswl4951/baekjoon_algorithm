#숨바꼭질 2
import sys
from collections import deque

def bfs():
    global result
    q=deque()
    q.append(n)
    dp[n]=0

    while q:
        x=q.popleft()
        if x==k: result+=1

        for nx in [x-1,x+1,x*2]:
            if 0<=nx<100001:
                if dp[nx]==-1 or dp[nx]>=dp[x]+1:
                    dp[nx]=dp[x]+1
                    q.append(nx)

n,k = map(int,sys.stdin.readline().split())
dp=[-1]*100001
result=0
bfs()
print(dp[k])
print(result)