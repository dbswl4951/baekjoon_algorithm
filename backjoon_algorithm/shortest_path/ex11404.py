#플로이드
'''
기본적인 플로이드 워셜 문제여서 쉽게 풀었다.
'''
import sys

def floyd():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

INF=int(1e9)
n=int(sys.stdin.readline().strip())
m=int(sys.stdin.readline().strip())
graph=[[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x,y,z=map(int,sys.stdin.readline().split())
    if graph[x][y]!=INF:    #노선이 여러개일 경우 더 적은 비용으로 업데이트
        z=min(z,graph[x][y])
    graph[x][y]=z
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:    #자기 자신으로 가는 거리는 0
            graph[i][j]=0
floyd() #플로이드 워셜 알고리즘 실행
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF:
            print(0,end=' ')
        else:
            print(graph[i][j],end=' ')
    print()