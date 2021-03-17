#파티
'''
다익스트라 알고리즘 사용
'''
import sys,heapq

def dijkstra(x):
    distance =[INF] * (n + 1)
    distance[x]=0
    q=[]
    heapq.heappush(q,(0,x))
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist: continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance

INF=int(1e9)
n,m,x=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
dist1=dijkstra(x)
result=[]
for i in range(1,n+1):
    if i==x: continue
    dist2=dijkstra(i)
    result.append(dist1[i]+dist2[x])
print(max(result))