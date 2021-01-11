#미래 도시
'''
플로이드 워셜 알고리즘
'''
import sys

INF = int(1e9)
n,m=map(int,sys.stdin.readline().split())
graph=[[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    graph[x][y]=1   #이동시간=1
    graph[y][x]=1   #양방향
x,k=map(int,sys.stdin.readline().split())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:    #자기 자신으로 가는 비용은 0
            graph[i][j]=0

#플로이드 워셜 알고리즘으로 모든 노드의 최단 경로 구함
for k in range(1,n+1):  #거쳐야 하는 지점
    for i in range(1,n+1):  #시작 지점
        for j in range(1,n+1):  #도착 지점
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
dist=graph[1][k]+graph[k][x]    #걸린 시간
if dist>=INF:   #도달 할 수 없는 경우 -1 출력
    print(-1)
else:
    print(dist)