#경로 찾기
'''
dfs
'''
import sys

def dfs(x):
    for i in range(n):  #한 노드x에 대해 경로가 있는 모든 i 탐색
        if graph[x][i]==1 and visited[x]==0:
            visited[i] = 1
            dfs(i)

n=int(sys.stdin.readline().strip())
graph=[]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
visited=[0 for _ in range(n)]
for i in range(n):
    dfs(i)  #한 행마다 방문 수행
    for j in range(n):
        if visited[j]==1:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()
    visited=[0 for _ in range(n)]   #방문한 노드가 있으면 1로 출력 후, 초기화