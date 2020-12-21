#DFS와 BFS
'''
쉽게 풀 수 있을 줄 알았지만..아니였다
양방향 관계를 나타내기 위해 2차원 리스트 사용한게 핵심!!
'''
from collections import deque

def dfs(v):
    print(v, end=' ')
    visited[v]=1    #방문하면 1로
    for i in range(1,n+1):
        if visited[i]==0 and relation[v][i]==1: #연결 노드 중 방문하지 않은게 있다면
            dfs(i)

def bfs(v):
    q=deque()
    q.append(v)
    visited[v]=0    #방문하면 0으로
    while q:
        v=q.popleft()
        print(v,end=' ')
        for i in range(1,n+1):
            if visited[i]==1 and relation[v][i]==1:
                visited[i]=0
                q.append(i)

n, m, v = map(int, input().split())
relation=[[0]*(n+1) for _ in range(n+1)]    #양방향 관계 표시 하기 위한 list
visited=[0 for _ in range(n+1)]    #1~n번까지의 방문 노드 저장
for i in range(m):
    x,y=map(int,input().split())
    relation[x][y]=1    #양방향으로 관계 설정 (1:연결되어있음)
    relation[y][x]=1

dfs(v)
print()
bfs(v)