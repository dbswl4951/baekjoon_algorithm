#음식물 피하기
'''
bfs 사용
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    global visited
    count=1
    q=deque()
    q.append([x,y])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and way[nx][ny]==1:
                visited[nx][ny]=1
                count+=1
                q.append([nx,ny])
    return count

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
            visited[i][j]=1
            result=max(result,bfs(i,j))
print(result)