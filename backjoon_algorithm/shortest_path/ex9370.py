#미확인 도착지
'''
[ 문제 요약 ]
1) 1~5까지 가는 최단거리에서 간선 2~3를 지나는지 확인
2) 2~3를 지나는 노드들 구하기

[ 문제 풀이 1 ]
가장 간단한 방법은 다익스트라를 3번 사용 하는 것
    => (1~2 최단거리) + (2~3 최단거리) + (3~5 최단거리)
But, 효율적이지 않음

[ 문제 풀이 2 ]
1) 가중치를 저장 할 때, 지나간 간선 2~3은 X2 한 뒤 -1
    나머지 간선은 X2 해 줌
2) 그 후 최단거리를 구했을 때, 최단거리가 홀수라면 2~3을 지나간 것이므로 정답
'''
import sys,heapq

def dijkstra(s):
    q=[]
    heapq.heappush(q,[0,s])
    distance = [float('inf')]*(n+1)
    distance[s]=0

    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist: continue
        for node in graph[now]:
            cost=graph[now][node]+dist
            if cost<distance[node]:
                distance[node]=cost
                heapq.heappush(q,[cost,node])
    return distance

t=int(sys.stdin.readline().strip())
for _ in range(t):
    n,m,t=map(int,sys.stdin.readline().split()) # 노드 수, 간선 수, 목적지 후보 수
    s,g,h=map(int,sys.stdin.readline().split()) # 시작 노드, 지나간 도로a, 지나간 도로b
    graph=[dict() for _ in range(n+1)]
    destination = [int(sys.stdin.readline().strip()) for _ in range(t)]
    for _ in range(m):
        a,b,d=map(int,sys.stdin.readline().split())
        graph[a][b]=d*2
        graph[b][a]=d*2

    # 지나간 간선은 홀수로 만들어 주기 위해 -1 해 줌
    graph[g][h]-=1
    graph[h][g]-=1
    distance=dijkstra(s)
    result=[]
    for d in destination:
        # 최단 거리가 홀수이면 g~h 또는 h~g 간선을 지나간 것이므로 정답
        if distance[d]%2==1: result.append(d)
    result.sort()
    for r in result: print(r,end=' ')
    print()