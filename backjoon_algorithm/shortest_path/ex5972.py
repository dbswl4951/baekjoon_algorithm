#택배 배송
import sys,heapq

def dijkstra():
    q=[]
    heapq.heappush(q,[0,1]) # [비용, 노드]
    distance[1] = 0

    while q:
        dist,now = heapq.heappop(q)
        # 현재 노드가 이미 처리 된 적이 있으면 패스
        if distance[now] < dist: continue
        for i in graph[now]:
            cost=dist+i[1]
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,[cost,i[0]])

n,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
distance=[int(1e9)]*(n+1)
for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append([b,c])  # [노드,비용]
    graph[b].append([a,c])
dijkstra()
print(distance[n])