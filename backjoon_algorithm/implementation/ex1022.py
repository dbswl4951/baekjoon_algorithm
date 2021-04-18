#소용돌이 예쁘게 출력하기
import sys

dx=[0,-1,0,1]
dy=[1,0,-1,0]

# board가 다 채워졌는지 체크
def check(board):
    for i in range(row):
        for j in range(col):
            if board[i][j]==0: return False
    return True

# 소용돌이 모양으로 숫자 넣기
def start(sx,sy):
    moveCnt,addCnt,number=1,0,2
    flag=0
    while True:
        for i in range(4):
            for j in range(moveCnt):
                nx,ny=sx+dx[i],sy+dy[i]
                if 0<=nx<=x2 and 0<=ny<=y2:
                    board[nx][ny]=number
                sx,sy=nx,ny
                number+=1
                if check(board):
                    flag=1
                    break
            addCnt+=1
            if flag: break
            if addCnt%2==0: moveCnt+=1
        if flag: break

x1,y1,x2,y2=map(int,sys.stdin.readline().split())
sx,sy=-x1,-y1   # 시작 지점
row,col=abs(x1-x2)+1,abs(y1-y2)+1
x1,y1,x2,y2=0,0,x2-x1,y2-y1
board=[[0]*col for _ in range(row)]
if 0<=sx<row and 0<=sy<col: board[sx][sy]=1

start(sx,sy)
maxVal=0
for b in board:
    maxVal=max(maxVal,max(b))
maxLen=len(str(maxVal))
for bo in board:
    for b in bo:
        if len(str(b))!=maxLen:
            for i in range(maxLen-len(str(b))):
                print(end=' ')
        print(b,end=' ')
    print()