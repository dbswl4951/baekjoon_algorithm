#마법사 상어와 토네이도
import math

dx=[0,1,0,-1]
dy=[-1,0,1,0]

# 범위 안에 있으면 모래 옮기기, 범위 밖이면 result에 더하기
def rangeCheck(x,y,nx,ny,p):
    global result
    board[x][y] -= p
    if 0<=nx<n and 0<=ny<n:
        board[nx][ny]+=p
    else:
        result+=p

n=int(input().strip())
board=[list(map(int,input().split())) for _ in range(n)]
x,y=n//2,n//2   # 시작 (x,y)
moveCnt,addCnt=1,0   # 한 방향으로 나가는 횟수
result,flag=0,0

for i in range(n//2+1):
    for j in range(4):
        addCnt += 1
        for k in range(moveCnt):
            nx,ny=x+dx[j],y+dy[j]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny]!=0:
                    # 확산 될 모래 양 구하기
                    p10,p7,p5,p2,p1=math.floor(board[nx][ny]*0.1),math.floor(board[nx][ny]*0.07),\
                                    math.floor(board[nx][ny]*0.05),math.floor(board[nx][ny] * 0.02),math.floor(board[nx][ny]*0.01)
                    a=board[nx][ny]-p5-2*(p10+p7+p2+p1)

                    ax,ay=nx+dx[j],ny+dy[j]     # a의 (x,y)좌표
                    nj1,nj3=(j+1)%4,(j+3)%4
                    # a,p5에 모래 옮길 수 있는지 확인 후, 옮기기
                    rangeCheck(nx,ny,ax,ay,a)
                    rangeCheck(nx,ny,ax+dx[j],ay+dy[j],p5)
                    # p1에 모래 옮길 수 있는지 확인 후, 옮기기
                    rangeCheck(nx,ny,x+dx[nj1],y+dy[nj1],p1)
                    rangeCheck(nx,ny,x+dx[nj3],y+dy[nj3],p1)
                    # p2,p7에 모래 옮길 수 있는지 확인 후, 옮기기
                    rangeCheck(nx,ny,nx+dx[nj1],ny+dy[nj1],p7)
                    rangeCheck(nx,ny,nx + dx[nj3], ny + dy[nj3],p7)
                    rangeCheck(nx,ny,nx + 2*(dx[nj1]), ny + 2*(dy[nj1]),p2)
                    rangeCheck(nx,ny,nx + 2*(dx[nj3]), ny + 2*(dy[nj3]), p2)
                    # p10에 모래 옮길 수 있는지 확인 후, 옮기기
                    rangeCheck(nx,ny,ax + dx[nj1], ay + dy[nj1], p10)
                    rangeCheck(nx,ny,ax + dx[nj3], ay + dy[nj3], p10)
                x,y=nx,ny
                if x==0 and y==0:
                    flag=1
                    break
        if flag: break
        if addCnt%2==0: moveCnt+=1
    if flag: break
print(result)