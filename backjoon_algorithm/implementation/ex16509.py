#장군
import sys
from collections import deque

dx=[[-1,-1,-1],[-1,-1,-1],[0,-1,-1],[0,1,1],[1,1,1],[1,1,1],[0,1,1],[0,-1,-1]]
dy=[[0,1,1],[0,-1,-1],[-1,-1,-1],[-1,-1,-1],[0,-1,-1],[0,1,1],[1,1,1],[1,1,1]]
dxx=[-3,-3,-2,2,3,3,2,-2]
dyy=[2,-2,-3,-3,-2,2,3,3]

def bfs():
    q = deque()
    q.append([sx,sy,0])
    visited = [[0]*10 for _ in range(11)]
    visited[sx][sy]=1
    flag = 0

    while q:
        if flag: break
        x,y,cnt = q.popleft()
        if x==kx and y==ky:
            print(cnt)
            flag=1
            break

        for i in range(8):
            if x+dxx[i]<0 or x+dxx[i]>9 or y+dyy[i]<0 or y+dyy[i]>8: continue
            nx, ny = x, y
            for j in range(3):
                nx,ny = nx+dx[i][j],ny+dy[i][j]
                if 0<=nx<=9 and 0<=ny<=8:
                    if j<2 and nx==kx and ny==ky: break
                    if j==2 and not visited[nx][ny]:
                        visited[nx][ny]=1
                        q.append([nx,ny,cnt+1])
                else: break
    if not flag: print(-1)

sx,sy = map(int,sys.stdin.readline().split())
kx,ky = map(int,sys.stdin.readline().split())
bfs()