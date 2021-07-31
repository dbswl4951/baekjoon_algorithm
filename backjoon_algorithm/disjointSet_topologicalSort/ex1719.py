#택배
'''
플로이드 와샬
'''
import sys

def floyd():
    for k in range(1,n+1):  # k : 거쳐가는 지점
        for i in range(1,n+1):
            for j in range(1,n+1):
                if distance[i][j]>distance[i][k]+distance[k][j]:
                    distance[i][j]=distance[i][k]+distance[k][j]
                    # 처음 들렸던 정점을 그대로 이어간다
                    result[i][j]=result[i][k]

INF=int(1e9)
n,m = map(int,sys.stdin.readline().split())
distance=[[INF]*(n+1) for _ in range(n+1)]
result=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    distance[a][b]=c
    distance[b][a]=c
    result[a][b]=b
    result[b][a]=a
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j: distance[i][j]=0
floyd()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j: print('-',end=' ')
        else: print(result[i][j],end=' ')
    print()