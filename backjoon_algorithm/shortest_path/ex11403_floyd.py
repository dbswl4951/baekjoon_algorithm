#경로 찾기
'''
플로이드-워셜
'''
import sys

n=int(sys.stdin.readline().strip())
graph=[]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
for k in range(n):
    for i in range(n):
        for j in range(n):
            #i->j바로 갈 수 있거나 k를 들려 i->k->j로 갈 수 있으면 i->j로 가는 경로 존재 (graph[i][j]=1)
            if graph[i][j]==1 or (graph[i][k]==1 and graph[k][j]==1):
                graph[i][j]=1
for g in graph:
    print(*g)