#암벽 등반
import sys
from collections import deque

n,t = map(int,sys.stdin.readline().split())
yArr = [[] for _ in range(200001)]
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    yArr[b].append(a)

q = deque()
q.append([0,0,0])   # (x,y,cnt)
while q:
    x,y,cnt = q.popleft()
    if y==t:
        print(cnt)
        sys.exit(0)

    for ny in range(y-2,y+3):
        if ny<0 or ny>t: continue
        for nx in range(x-2,x+3):
            if nx not in yArr[ny]: continue
            yArr[ny].remove(nx)
            q.append([nx,ny,cnt+1])
print(-1)