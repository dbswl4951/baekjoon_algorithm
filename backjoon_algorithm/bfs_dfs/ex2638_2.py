#치즈
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    q=deque()
    q.append([0,0])
    visited=[[0]*m for _ in range(n)]   # 방문 체크
    visited[0][0]=1
    check=[[0]*m for _ in range(n)]     # 공기에 노출된 면 개수 count

    # 공기와 접촉 한 면 세기
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if board[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append([nx,ny])
                else:
                    check[nx][ny]+=1

    # 치즈 녹이기
    for i in range(n):
        for j in range(m):
            if check[i][j]>=2:
                board[i][j]=0

n,m=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
result=0
while True:
    result+=1
    bfs()
    cnt=0
    for b in board:
        cnt+=sum(b)
    if cnt==0: break
print(result)