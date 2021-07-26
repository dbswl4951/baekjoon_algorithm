#가스관
import sys,copy
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def setBlock(t):
    if t==0: return '|'
    elif t==1: return '-'
    elif t==2: return '+'
    elif t==3: return '1'
    elif t==4: return '2'
    elif t==5: return '3'
    else: return '4'

def dfs(board,x,y,dirX,dirY,visited):
    if board[x][y]=='.': return False

    block=board[x][y]
    if block=='|':


r,c=map(int,sys.stdin.readline().split())
board=[list(sys.stdin.readline().split()) for _ in range(r)]
mx,my=0,0
for i in range(r):
    for j in range(c):
        if board[i][j]=='M': mx=i; my=j

for i in range(r):
    for j in range(c):

        # 빈 칸을 발견하면 임의의 블록 (7가지)를 놓는다
        if board[i][j]=='.':
            for t in range(7):
                copyBoard = copy.deepcopy(board)
                copyBoard[i][j]=setBlock(t)
                visited=[[0]*c for _ in range(r)]
                visited[mx][my]=1
                # 시작지점에서 연결 된 블록 찾기
                for d in range(4):
                    nx,ny=mx+dx[i],my+dy[i]
                    if copyBoard[nx][ny]!='.':
                        dfs(copyBoard,nx,ny,dx[i],dy[i],visited)

'''
#가스관
import sys,copy
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def setBlock(t):
    if t==0: return '|'
    elif t==1: return '-'
    elif t==2: return '+'
    elif t==3: return '1'
    elif t==4: return '2'
    elif t==5: return '3'
    else: return '4'

def bfs(board):
    q=deque()
    q.append([mx,my])
    visited=[[0]*c for _ in range(r)]
    visited[mx][my]=1

    while q:
        x,y=q.popleft()
        if board[x][y]=='Z' : continue
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<r and 0<=ny<c and board[nx][ny]!='.' and board[nx][ny]!='Z' and not visited[nx][ny]:
                block=board[nx][ny]


r,c=map(int,sys.stdin.readline().split())
board=[list(sys.stdin.readline().split()) for _ in range(r)]
mx,my=0,0
for i in range(r):
    for j in range(c):
        if board[i][j]=='M': mx=i; my=j

for i in range(r):
    for j in range(c):
        # 빈 칸을 발견하면 임의의 블록 (7가지)를 놓는다
        if board[i][j]=='.':
            copyBoard=copy.deepcopy(board)
            for t in range(7):
                copyBoard[i][j]=setBlock(t)
                bfs(copyBoard)

'''