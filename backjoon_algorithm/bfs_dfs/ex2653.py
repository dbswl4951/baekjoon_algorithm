#안정된 집단
import sys
from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next]=1
                if now in result:
                    result[now].append(next)
                else:
                    result[now]=[next]
                q.append(next)

n = int(sys.stdin.readline().strip())
visited =[0]*(n+1)
graph = [[] for _ in range(n+1)]
for i in range(n):
    like = []
    temp = list(map(int,sys.stdin.readline().split()))
    for j in range(n):
        if temp[j]==0:
            like.append(j + 1)
            if i!=j: graph[i+1].append(j+1)
    if len(like)==1:
        print(0)
        sys.exit(0)

result = {}
for i in range(1,n+1):
    if not visited[i]:
        bfs(i)

sorted(result)
if result:
    print(len(result))
    for i in range(1,n+1):
        if i in result:
            print(i,end=' ')
            for value in result[i]:
                print(value,end=' ')
            print()
else: print(0)