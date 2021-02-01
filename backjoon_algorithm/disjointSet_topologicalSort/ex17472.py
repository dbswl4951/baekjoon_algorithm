#다리 만들기2
'''
1. 섬에 라벨링 하기
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#섬 번호 붙이기
def bfs(x,y,num):
    visited[x][y]=1
    board[x][y]=num
    q=deque()
    q.append([x,y])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <=nx<n and 0<=ny<m and board[nx][ny]==1 and visited[nx][ny]==0:
                visited[nx][ny]=1
                board[nx][ny]=num
                q.append([nx,ny])

#각 섬 별로 최소 거리 구하기
def getDistance(board):
    table=[[float('inf')]*m for _ in range(n)]

n,m=map(int,sys.stdin.readline().split())
board=[]
for _ in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))
visited=[[0]*m for _ in range(n)]
num=1
#섬 라벨링
for i in range(n):
    for j in range(m):
        if board[i][j]==1 and visited[i][j]==0:
            bfs(i,j,num)
            num += 1
minDistance=[[float('inf')]*num for _ in range(num)]
#섬 연결하는 최소 거리 구하기
table=getDistance(board)
