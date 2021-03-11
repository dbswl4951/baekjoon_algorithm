#키 순서
'''
플로이드 와샬 문제

자신이 갈 수 있는 노드들은 자기보다 큰 사람들
자신에게 오는 경로가 있는 노드들은 자기보다 작은 사람들
이 둘의 합이 자신을 제외한 N-1인 경우 자신의 순서를 알 수 있음
'''
import sys

def floyd():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

INF=int(1e9)
n,m=map(int,sys.stdin.readline().split())
graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j: graph[i][j]=0
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a][b]=1
floyd()
result=0
for i in range(1,n+1):
    cnt=0
    for j in range(1,n+1):
        if graph[i][j]!=0 and graph[i][j]!=INF:
            cnt+=1
        if graph[j][i]!=0 and graph[j][i]!=INF:
            cnt+=1
    if cnt==n-1:
        result+=1
print(result)