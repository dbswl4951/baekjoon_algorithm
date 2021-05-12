#녹색 옷 입은 애가 젤다지?
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    q=deque()
    q.append([0,0])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny]==-1:
                    visited[nx][ny]=visited[x][y]+board[nx][ny]
                    q.append([nx,ny])
                elif visited[nx][ny]>visited[x][y]+board[nx][ny]:
                    visited[nx][ny]=visited[x][y]+board[nx][ny]
                    q.append([nx,ny])

num=1
while True:
    n=int(sys.stdin.readline().strip())
    if n==0: break
    board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    visited=[[-1]*n for _ in range(n)]
    visited[0][0]=board[0][0]
    bfs()
    print("Problem",num,end='')
    print(":",visited[n-1][n-1])
    num+=1