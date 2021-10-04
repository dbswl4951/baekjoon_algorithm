#세부
'''
1차 다익스트라로 풀이 => 시간 초과

BFS + 이분탐색을 이용해야 풀 수 있음 (노드가 최대 10만개, 간선이 30만개 ..)
이분탐색을 이용해 제한 무게를 설정한 뒤, 해당 무게로 목표점에 도달할 수 있는지 BFS로 체크
'''
import sys
from collections import deque

def bfs(limit):
    q = deque()
    q.append(s)
    visited = [0]*(n+1)
    visited[s] = 1

    while q:
        now = q.popleft()
        if now == e: return 1

        for i in graph[now]:
            if not visited[i[0]] and i[1]>=limit:
                visited[i[0]]=1
                q.append(i[0])
    return 0

n,m = map(int,sys.stdin.readline().split())
s,e = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

result = 0
left,right = 1,1000000
while left<=right:
    # 최소 무게
    mid = (left+right)//2

    # 건널 수 있다면, 더 큰 limit를 구하기 위해 left 키움
    if bfs(mid):
        result = mid
        left = mid+1
    else:
        right = mid-1
print(result)