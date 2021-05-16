#오민식의 고민
'''
O(V*E) => O(V^3) (V:정점의 개수)

[ check 할 점 ]
1. 벨만포드 => 최단 거리 구함
    우리는 최대 비용을 구해야 하므로 얻는 돈을 -, 쓰는 비용을 +해서 dist에 저장하고,
    dist가 최소가 되도록 함
    답 출력시, -를 붙여줘야 함
2. 순환되는 정점을 visited=1로 저장
    벨만포드로 모든 노드 돈 후, 끝점이 순환에 포함되어있는지 (visited[end]==1) 확인
3. INF=int(1e9)로 하면 4%에서 틀렸습니다 나옴
    무한대는 float(inf)로 하자!
'''
import sys
from collections import deque

def bellmanFord():
    # i : 순환 횟수
    for i in range(n):
        # now : 시작 지점
        for now in range(n):
            for j in graph[now]:
                # 얻는 비용 -, 쓰는 비용 + 해줌 => 최솟값으로 계속 갱신
                if dist[j[0]]>dist[now]+j[1]-gain[j[0]]:
                    dist[j[0]]=dist[now]+j[1]-gain[j[0]]
                    if i==n-1:
                        visited[now]=1
                        q.append(now)

def bfs():
    while q:
        x=q.popleft()
        for i in graph[x]:
            # 순환 사이클에 연결 된 노드는 모두 visited 처리 해줌
            if not visited[i[0]]:
                visited[i[0]]=1
                q.append(i[0])

INF = float('inf')
n,start,end,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((b,c))

gain=list(map(int,sys.stdin.readline().split()))
dist=[INF]*n
dist[start]=-gain[start]
visited=[0]*n
q=deque()
bellmanFord()
bfs()

# 도착점이 순환에 포함되어 있으면 Gee 출력
if visited[end]: print('Gee')
elif dist[end]==INF: print('gg')
else: print(-dist[end])