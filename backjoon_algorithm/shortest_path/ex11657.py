#타임머신
'''
벨만포드 알고리즘
'''
import sys

def bellmanFord(start):
    distance[start]=0   #시작지점 0으로 초기화
    for i in range(1,n+1):  #라운드 반복
        for j in range(1,m+1):  #모든 간선 검사
            now,next,cost=edge[j][0],edge[j][1],edge[j][2]  #현재노드, 다음노드, 시간
            if distance[now]!=INF and distance[next]>distance[now]+cost:
                distance[next]=distance[now]+cost
                if i==n:    #음수 사이클 발생
                    return True
    return False    #음수 사이클 없음

INF=int(1e9)
n,m=map(int,sys.stdin.readline().split())   #도시 개수, 노선 개수
edge=[0]
for _ in range(m):
    x,y,z=map(int,sys.stdin.readline().split())
    edge.append((x,y,z))    #(출발노드,도착노드,시간)
distance=[INF]*(n+1)
cycle=bellmanFord(1)  #1번 노드부터 시작. 벨만포드 알고리즘 실행
if not cycle:    #음수 사이클 없음
    for i in range(2,n+1):
        if distance[i]==INF: print(-1)
        else: print(distance[i])
else: print(-1)     #음수 사이클 있음