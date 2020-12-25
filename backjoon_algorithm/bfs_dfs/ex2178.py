#미로 탐색
'''
최소 칸 수 => bfs 사용
visited에 시작점으로 부터의 거리를 넣고, 맨마지막 visited[n-1][m-1]을 구한다.
한 번에 쉽게 풀었다.
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    global visited
    q=deque()
    q.append([x,y])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and maze[nx][ny]==1 and visited[nx][ny]==0:
                visited[nx][ny]=visited[x][y]+1
                q.append([nx,ny])
    return visited[n-1][m-1]

n,m = map(int,sys.stdin.readline().split())
maze=[]
for _ in range(n):
    maze.append(list(map(int,sys.stdin.readline().strip())))
visited=[[0]*m for _ in range(n)]
visited[0][0]=1
result=0
print(bfs(0,0))