#특정한 최단 경로
'''
다익스트라를 3번 사용
경우1) 1->v1->v2->n
경우2) 1->v2->v1->n

경우1만 생각하고 경우2는 생각 못해서 시간 많이 잡아먹음
경우2를 생각 안했을 경우의 반례
4 5
1 3 4
1 4 6
3 4 1
4 2 2
2 3 3
2 3
====9
'''
import sys,heapq

def dijkstra(start):
    distance =[INF]*(n+1)
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start))   #(거리,노드)
    while q:
        dist,now=heapq.heappop(q)   #dist:거리, now:현재 노드
        for i in graph[now]: #현재 노드와 연결된 모든 노드들 검사. i[0]=노드, i[1]=거리
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance

INF=int(1e9)
n,e=map(int,sys.stdin.readline().split())   #정점 개수, 간선 개수
graph=[[] for _ in range(n+1)]
for _ in range(e):
    x,y,z=map(int,sys.stdin.readline().split()) #출발노드, 도착노드, 거리
    graph[x].append((y,z))  #양방향
    graph[y].append((x,z))
v1,v2=map(int,sys.stdin.readline().split()) #반드시 거쳐야 하는 노드 2개
dist1=dijkstra(1)
dist2=dijkstra(v1)
dist3=dijkstra(v2)
if dist1[v1]==INF or dist2[v2]==INF or dist3[-1]==INF:
    print(-1)
else:
    #1->v1->v2->n 경우와 1->v2->v1->n 경우 중 더 작은 값 선택
    result=min(dist1[v1]+dist2[v2]+dist3[-1],dist1[v2]+dist3[v1]+dist2[-1])
    print(result)