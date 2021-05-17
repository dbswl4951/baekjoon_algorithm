#최소비용 구하기2
import sys,heapq

def dijkstra():
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    path[start].append(start)

    while q:
        dist,now=heapq.heappop(q)
        for i in graph[now]:
            cost=dist+i[1]
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
                path[i[0]]=[]
                for p in path[now]:
                    path[i[0]].append(p)
                path[i[0]].append(i[0])

n=int(sys.stdin.readline().strip())
m=int(sys.stdin.readline().strip())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
start,end=map(int,sys.stdin.readline().split())
distance=[float('inf')]*(n+1)
path=[[] for _ in range(n+1)]
dijkstra()
print(distance[end])
print(len(path[end]))
print(*path[end])