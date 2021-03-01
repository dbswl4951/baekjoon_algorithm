#이분 그래프
import sys
from collections import deque

def bfs(node,graph,visited):
    q=deque()
    q.append(node)
    visited[node]=1
    while q:
        now=q.popleft()
        for next in graph[now]:
            if visited[next] == 0:
                q.append(next)
                visited[next]=-visited[now]
            elif visited[next]==visited[now]:
                return 1
    return 0

k=int(sys.stdin.readline().strip())
for _ in range(k):
    v,e=map(int,sys.stdin.readline().split())
    graph=[[] for _ in range(v+1)]
    for _ in range(e):
        a,b=map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    visited=[0 for _ in range(v+1)]
    flag=0
    #그래프가 연결 되지 않은 경우도 있으므로, for문으로 전체 탐색
    for i in range(1,v+1):
        if not visited[i]:
            flag=bfs(i,graph,visited)
            if flag: break
    if not flag: print("YES")
    else: print("NO")