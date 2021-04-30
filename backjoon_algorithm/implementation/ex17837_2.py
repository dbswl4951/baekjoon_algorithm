#새로운 게임2
from collections import deque

dx=[0,0,-1,1]
dy=[1,-1,0,0]

# 방향 반대로 바꾸기
def changeDirection(d):
    if d==0: return 1
    elif d==1: return 0
    elif d==2: return 3
    else: return 2

# 말이 4개 이상인지 확인
def checkCnt():
    for i in range(n):
        for j in range(n):
            if len(check[i][j])>=4:
                return True
    return False

def turn():
    for i in range(k):
        x,y,d=chess[i]
        nx,ny=x+dx[d],y+dy[d]
        idx=check[x][y].index(i)

        # 범위 밖 or 파란 칸
        if not 0<=nx<n or not 0<=ny<n or board[nx][ny]==2:
            d=changeDirection(d)
            nx,ny=x+dx[d],y+dy[d]
            chess[i][2]=d

        # 흰 칸 or 빨간 칸
        if 0<=nx<n and 0<=ny<n and board[nx][ny]!=2:
            temp=check[x][y][idx:]
            # 빨간 칸이면 순서 거꾸로 바꾸기
            if board[nx][ny]==1:
                temp=temp[::-1]
            # 말 이동
            check[nx][ny].extend(temp)
            check[x][y]=check[x][y][:idx]
            # 말 이동 후, 갱신
            for t in temp:
                chess[t][0],chess[t][1]=nx,ny

        # 말이 4마리 이상 모였는지 체크
        if checkCnt(): return True
    return False

n,k=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
check=[[[] for _ in range(n)] for _ in range(n)]     # board 위에 chess 저장
chess=[]
for i in range(k):
    x,y,d=map(int,input().split())
    chess.append([x-1,y-1,d-1])
    check[x-1][y-1].append(i)

reuslt=0
while reuslt<=1000:
    reuslt += 1
    if turn(): break
if reuslt==1001: print(-1)
else: print(reuslt)