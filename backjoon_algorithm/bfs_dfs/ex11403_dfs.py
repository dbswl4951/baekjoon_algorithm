#경로 찾기
'''
bfs
'''
import sys
from collections import deque

def bfs(x):
    visited=[0]*n
    q=deque()
    q.append(x)
    while q:
        x=q.popleft()
        for i in range(n):
            if graph[x][i]==1 and visited[i]==0:
                visited[i]=1
                q.append(i)
    return visited

n=int(sys.stdin.readline().strip())
graph=[]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
    visited=bfs(i)
    print(*visited)
