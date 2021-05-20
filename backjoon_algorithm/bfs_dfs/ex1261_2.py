#알고스팟
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    q=deque()
    q.append([0,0])
    visited=[[0]*m for _ in range(n)]
    visited[0][0]=1
    breakCnt=[[0]*m for _ in range(n)]      # 부순 벽 개수 저장

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append([nx,ny])
                    if board[nx][ny]==1: breakCnt[nx][ny]=breakCnt[x][y] + 1
                    else: breakCnt[nx][ny]=breakCnt[x][y]
                # 이미 방문한 곳일 때
                else:
                    # 벽을 더 적게 부순걸로 갱신 + 큐에 삽입
                    if board[nx][ny]==0 and breakCnt[x][y]<breakCnt[nx][ny]:
                        breakCnt[nx][ny]=breakCnt[x][y]
                        q.append([nx,ny])
                    elif board[nx][ny]==1 and breakCnt[x][y]+1<breakCnt[nx][ny]:
                        breakCnt[nx][ny]=breakCnt[x][y]+1
                        q.append([nx, ny])
    return breakCnt[n-1][m-1]

m,n=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
print(bfs())