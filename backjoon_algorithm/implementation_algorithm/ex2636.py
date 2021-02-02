#치즈
'''
bfs로 (0,0)부터 탐색 시작
1) 0(빈 칸)을 만나면 큐에 삽입
2) 치즈의 가장자리 만나면 큐에 삽입 하지 않고 치즈를 1->2로 변경

가장 자리 인지 아닌지 판별 하는 법을 몰라서 힌트 참고!
가장자리를 판별하는 핵심만 생각하기 까다로웠고 나머지는 수월했음
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#치즈 가장자리 녹이기 / 다 녹았는지 확인
def melting():
    global count,time
    melt=deque()
    time+=1
    cheeseCnt=0
    for i in range(n):
        for j in range(m):
            if board[i][j]==2:
                melt.append([i,j])
                cheeseCnt+=1
                count-=1
    if count==0:
        print(time)
        print(cheeseCnt)
    else:
        while melt:
            x,y=melt.popleft()
            board[x][y]=0

#치즈 가장 자리 판별
def bfs():
    visited=[[0]*m for _ in range(n)]
    q=deque()
    q.append([0,0])
    visited[0][0]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
                visited[nx][ny]=1
                if board[nx][ny]==0:
                    q.append([nx,ny])
                elif board[nx][ny]==1:
                    board[nx][ny]=2 #가장자리임을 표시
    #print(board)

n,m=map(int,sys.stdin.readline().split())   #가로,세로
board=[]
count,time=0,0
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))
    for j in range(m):
        if board[i][j]==1:
            count+=1
while True:
    bfs()
    melting()
    if count==0: break
