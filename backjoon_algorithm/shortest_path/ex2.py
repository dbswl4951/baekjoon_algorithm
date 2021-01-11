#전보
'''
다익스트라 알고리즘 사용
'''
import sys,heapq

#다익스트라 알고리즘 수행
def dijkstra(start):
    q=[]    #우선 순위 큐 (비용,노드)
    distance[start]=0   #시작 지점은 거리 0으로 설정
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]<dist:  #현재 노드가 이미 처리된 적 있으면 무시
            continue
        for i in graph[now]:    #i:(노드,비용)
            cost=dist+i[1]  #새로 구한 비용
            if cost<distance[i[0]]: #현재 노드(i[0])을 거쳐 가는게 거리가 더 짧은 경우
                distance[i[0]]=cost
                q.append((cost,i[0]))

INF=int(1e9)
n,m,c=map(int,sys.stdin.readline().split())
graph=[[] for i in range(n+1)]
for i in range(m):
    x,y,z=map(int,sys.stdin.readline().split())
    graph[x].append((y,z))  #(노드,비용)
count,maxDist=0,0
distance=[INF]*(n+1)    #최단 거리 저장 테이블
dijkstra(c) #다익스트라 알고리즘 수행
for d in distance:
    if d!=INF:  #도달 할 수 있는 노드인 경우
        count+=1
        maxDist=max(maxDist,d)
print(count-1,maxDist)