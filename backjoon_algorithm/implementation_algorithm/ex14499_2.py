#주사위 굴리기
import sys

dx=[0,0,-1,1]
dy=[1,-1,0,0]

# 동쪽n이동
def moveRight(dice):
    return [dice[4],dice[1],dice[5],dice[3],dice[2],dice[0]]

# 서쪽n이동
def moveLeft(dice):
    return [dice[5],dice[1],dice[4],dice[3],dice[0],dice[2]]

# 북쪽 이동
def moveUp(dice):
    return [dice[1],dice[2],dice[3],dice[0],dice[4],dice[5]]

# 남쪽 이동
def moveDown(dice):
    return [dice[3],dice[0],dice[1],dice[2],dice[4],dice[5]]

# board가 0이면 주사위의 값이 board로 복사, 0이 아닌 경우 board->주사위로 복사
def copyNumber(dice,x,y):
    # 주사위 바닥 값 -> board로 복사 됨
    if board[x][y]==0:
        board[x][y] = dice[2]
    # board -> 주사위 바닥으로 복사 됨
    else:
        dice[2]=board[x][y]
        board[x][y]=0

def gameStart(x,y):
    # [상단,앞,바닥,뒤,서,동]
    dice=[0,0,0,0,0,0]
    for order in orders:
        dir=order-1
        nx,ny=x+dx[dir],y+dy[dir]
        if 0<=nx<n and 0<=ny<m:
            if dir==0:
                dice=moveRight(dice)
            elif dir==1:
                dice=moveLeft(dice)
            elif dir==2:
                dice=moveUp(dice)
            elif dir==3:
                dice = moveDown(dice)
            copyNumber(dice, nx, ny)
            print(dice[0])
            x,y=nx,ny

n,m,x,y,k=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
orders=list(map(int,sys.stdin.readline().split()))
gameStart(x,y)