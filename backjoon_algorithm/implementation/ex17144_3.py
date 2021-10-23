#미세먼지 안녕!

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 미세먼지 확산
def spreadDust():
    spreadBoard = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if board[i][j]>0:
                dust,cnt = board[i][j] // 5, 0
                for k in range(4):
                    ni,nj = i+dx[k],j+dy[k]
                    if 0<=ni<r and 0<=nj<c and board[ni][nj]!=-1:
                        spreadBoard[ni][nj] += dust
                        cnt += 1
                board[i][j] -= dust*cnt

    for i in range(r):
        for j in range(c):
            board[i][j] += spreadBoard[i][j]

# 아래로 공기청정기 작동
def moveDown(sx,sy,ex,ey):
    for x in range(ex,sx,-1):
        if x==-1: continue
        board[x][sy] = board[x-1][sy]

# 왼쪽으로 공기청정기 작동
def moveLeft(sx,sy,ex,ey):
    for y in range(ey,sy):
        board[sx][y] = board[sx][y+1]

# 위쪽으로 공기청정기 작동
def moveUp(sx,sy,ex,ey):
    for x in range(ex,sx):
        board[x][sy] = board[x+1][sy]

# 오른쪽으로 공기청정기 작동
def moveRight(sx,sy,ex,ey):
    for y in range(ey,sy,-1):
        board[sx][y] = board[sx][y-1]
    board[sx][sy] = 0

r,c,t = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(r)]
airfresh = []
for i in range(r):
    for j in range(c):
        if board[i][j] == -1: airfresh.append(i)

for _ in range(t):
    # 미세먼지 확산
    spreadDust()

    # 공기청정기 작동
    for idx,ax in enumerate(airfresh):
        # 위쪽 공기청정기
        if idx==0:
            moveDown(0,0,ax-1,0)
            moveLeft(0,c-1,0,0)
            moveUp(ax,c-1,0,c-1)
            moveRight(ax,1,ax,c-1)
        # 아래쪽 공기청정기
        else:
            moveUp(r-1,0,ax+1,0)
            moveLeft(r-1,c-1,r-1,0)
            moveDown(ax,c-1,r-1,c-1)
            moveRight(ax,1,ax,c-1)

result = 0
for i in range(r):
    for j in range(c):
        if board[i][j]>0: result += board[i][j]
print(result)