#트리의 지름
'''
다익스트라 2번 사용
1. 1번 노드 (root)부터 가장 먼 노드(x) 찾기
2. x로부터 가장 먼 노드(y) 찾기
3. x~y 사이의 거리 return
'''
import sys,heapq

def dijkstra(start):
    distance=[int(1e9)]*(n+1)
    distance[start]=0
    q=[]    # (거리,노드)
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        for i in graph[now]:
            d=dist+i[1]
            if distance[i[0]]>d:
                distance[i[0]]=d
                heapq.heappush(q,(d,i[0]))
    return distance

n=int(sys.stdin.readline().strip())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
distance=dijkstra(1)
node=distance.index(max(distance[1:]))
distance=dijkstra(node)
print(max(distance[1:]))