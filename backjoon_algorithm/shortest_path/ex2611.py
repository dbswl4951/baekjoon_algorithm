#자동차경주
'''
2가지 풀이 가능 (다익스트라, 위상정렬)
다익스트라 사용
'''
import sys,heapq

def dijkstra():
    global result
    q=[]
    heapq.heappush(q,[0,1])
    while q:
        dist,now = heapq.heappop(q)
        if dist>result and now==1:
            result=dist
            continue
        if distance[now] > dist: continue

        for i in graph[now]:
            cost = dist+i[1]
            if cost>distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,[cost,i[0]])
                path[i[0]]=now

n=int(sys.stdin.readline().strip())
m=int(sys.stdin.readline().strip())
graph=[[] for _ in range(m+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
distance,path = [0]*(n+1), [0]*(n+1)
result=0
dijkstra()
print(result)
temp,idx=[1],1
while True:
    node = path[idx]
    temp.append(node)
    if node==1: break
    idx=node
for i in range(len(temp)-1,-1,-1): print(temp[i], end=' ')