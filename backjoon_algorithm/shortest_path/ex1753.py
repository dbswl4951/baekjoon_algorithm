#최단경로
'''
기본적인 다익스트라 알고리즘이여서 쉽게 풀었음
'''
import sys,heapq

def dijkstra(start):
    distance = [INF] * (v + 1)
    distance[k] = 0  # 시작지점 경로 값은 0
    q=[]
    heapq.heappush(q,(0,start)) #(거리,노드)
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:  #현재 노드가 이미 처리된 적 있으면 무시
            continue
        for i in graph[now]:    #i:(노드,거리)
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance

INF=int(1e9)
v,e=map(int,sys.stdin.readline().split())   #정점 개수, 간선 개수
k=int(sys.stdin.readline().strip()) #시작 노드
graph=[[]*(v+1) for _ in range(v+1)]
for _ in range(e):
    x,y,z=map(int,sys.stdin.readline().split())
    graph[x].append((y,z))
distance =dijkstra(k)
for i in range(1,v+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])