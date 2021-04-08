#여행 가자
'''
플로이드 워셜 사용
'''
import sys

def floyd():
    for k in range(1,n+1):  # k : 거쳐가는 노드
        for i in range(1,n+1):  # i : 시작 노드
            for j in range(1,n+1):  # j : 도착 노드
                if graph[i][k]+graph[k][j]<graph[i][j]:
                    graph[i][j]=graph[i][k]+graph[k][j]

INF=int(1e9)
n=int(sys.stdin.readline().strip())
m=int(sys.stdin.readline().strip())
graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0
for i in range(1,n+1):
    temp=[0]+list(map(int,sys.stdin.readline().split()))
    for j in range(1,n+1):
        if temp[j]==1:
            graph[i][j]=1
            graph[j][i]=1
plan=list(map(int,sys.stdin.readline().split()))
floyd()
for i in range(m-1):
    if graph[plan[i]][plan[i+1]]==INF:
        print('NO')
        sys.exit(0)
print('YES')