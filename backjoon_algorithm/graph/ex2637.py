#장난감 조립
import sys
from collections import deque

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n+1)]
needs = [[0]*(n+1) for _ in range(n+1)]
indegree = [0]*(n+1)
q = deque()
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[b].append([a,c])
    indegree[a] += 1
# 진입차수 0인 애들 q에 넣기
for i in range(1,n+1):
    if indegree[i]==0: q.append(i)

while q:
    now = q.popleft()
    for next,cnt in graph[now]:
        # 기본 부품이라면
        if needs[now].count(0) == n+1:
            needs[next][now] += cnt
        # 중간 부품, 완제품이라면
        else:
            for i in range(1,n+1):
                needs[next][i] += needs[now][i]*cnt
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)
for i in range(1,n+1):
    if needs[n][i]>0:
        print(i,needs[n][i])