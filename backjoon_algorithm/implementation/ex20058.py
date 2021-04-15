#마법사 상어와 파이어스톰
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 시계방향으로 90도 회전
def rotateBoard(board):
    bLen=len(board)
    temp=[[0]*bLen for _ in range(bLen)]
    for i in range(bLen):
        for j in range(bLen):
            temp[j][bLen-i-1]=board[i][j]
    return temp

def getRotatedBorad(level):
    x,y=0,0
    l=2**level
    tempBoard=[[0]*l for _ in range(l)]
    while x+l<=n:
        while y+l<=n:
            for i in range(l):
                for j in range(l):
                    tempBoard[i][j]=board[i+x][j+y]
            tempBoard=rotateBoard(tempBoard)
            for i in range(l):
                for j in range(l):
                    board[i+x][j+y]=tempBoard[i][j]
            #for b in board:
            #    print(*b)
            y+=l
        x+=l
        y=0

# 인접한 칸이 2개 이하면 얼음 양-=1
def checkSideIce(x,y):
    global melting
    cnt=0
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n and board[nx][ny]!=0:
            cnt+=1
            if cnt>2: break
    if cnt<=2: melting.append([x,y])

# 가장 큰 덩어리가 차지하는 칸의 개수 구하기
def bfs(x,y):
    global iceCnt
    q=deque()
    cnt=1
    q.append([x, y])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]!=0 and visited[nx][ny]==0:
                cnt+=1
                q.append([nx,ny])
                visited[nx][ny]=1
    iceCnt=max(iceCnt,cnt)

N,Q=map(int,sys.stdin.readline().split())
n=2**N
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
levels=list(map(int,sys.stdin.readline().split()))

for level in levels:
    melting=deque()
    # 시계방향으로 90도 회전
    if level>0:
        getRotatedBorad(level)
    # 인접한 얼음 칸 갯수 2개 이하면 얼음 양-=1
    for i in range(n):
        for j in range(n):
            if board[i][j]!=0:
                checkSideIce(i,j)
    for x,y in melting:
        board[x][y]-=1

iceSum,iceCnt=0,0
for b in board:
    iceSum+=sum(b)
visited=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] != 0 and visited[i][j]==0:
            visited[i][j]=1
            bfs(i,j)
print(iceSum)
print(iceCnt)