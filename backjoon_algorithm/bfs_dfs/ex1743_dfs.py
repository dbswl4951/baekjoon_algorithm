#음식물 피하기
'''
dfs 사용

dfs,bfs 문제 알고리즘이나 풀이는 거의 맞는데 자꾸 이상 한 곳에서 실수 한다..
'''
import sys
sys.setrecursionlimit(40000)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y):
    global visited,count
    visited[x][y] = 1
    count+=1
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and way[nx][ny]==1:
            dfs(nx,ny)

n,m,k=map(int,sys.stdin.readline().split())
way=[[0]*m for _ in range(n)]
for _ in range(k):
    x,y=map(int,sys.stdin.readline().split())
    way[x-1][y-1]=1 #음식물이 떨어진 자리는 1로 설정
visited=[[0]*m for _ in range(n)]
result=0
for i in range(n):
    for j in range(m):
        if way[i][j]==1 and visited[i][j]==0:
            count = 0
            dfs(i,j)
            result=max(result,count)
print(result)