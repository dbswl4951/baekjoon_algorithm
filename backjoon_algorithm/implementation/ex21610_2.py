#마법사 상어와 비바라기
from collections import deque

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

# 구름 이동 + 비 내리기
def moveAndRain(d,s):
    cLen = len(cloud)

    # 구름 이동
    while cLen:
        x,y = cloud.popleft()
        nx,ny = x+dx[d]*s,y+dy[d]*s
        while nx<0 or nx>=n:
            if nx<0: nx+=n
            elif nx>=n: nx-=n
        while ny<0 or ny>=n:
            if ny<0: ny+=n
            elif ny>=n: ny-=n

        cloud.append([nx,ny])
        cBoard[x][y] = 0
        cLen -= 1

    # 비 내리기
    for cx,cy in cloud:
        board[cx][cy] += 1
        cBoard[cx][cy] = 1

# 물 복사 버그
def waterMagic():
    for x,y in cloud:
        cnt = 0
        # 대각선 방향 check
        for i in range(1,8,2):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]>0:
                cnt += 1
        board[x][y] += cnt

# 구름 새로 생성 + 물 줄어들기
def makeNewClouds():
    newClouds = deque()

    for i in range(n):
        for j in range(n):
            if board[i][j]>=2:
                if cBoard[i][j]==0:
                    newClouds.append([i,j])
                    board[i][j] -= 2
                    cBoard[i][j] = 1
                else:
                    cBoard[i][j] = 0
    return newClouds,cBoard

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
moves = [list(map(int,input().split())) for _ in range(m)]
cloud = deque()
cBoard = [[0]*n for _ in range(n)]  # 구름이 있는지 나타냄
cloud.append([n-1,0]); cloud.append([n-1,1])
cloud.append([n-2,0]); cloud.append([n-2,1])
result = 0

for move in moves:
    # 구름 이동 + 비 내리기
    moveAndRain(move[0]-1,move[1])
    # 물복사 버그
    waterMagic()
    # 구름 새로 생성 + 물 줄어들기
    cloud,cBoard = makeNewClouds()

for i in range(n):
    result += sum(board[i])
print(result)