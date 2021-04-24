#청소년 상어
import copy

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

# 물고기 이동
def moveFishes(board,sx,sy):
    for k in range(1,17):
        flag=0
        for i in range(4):
            for j in range(4):
                if board[i][j][0]==k:
                    dir=board[i][j][1]
                    for _ in range(8):
                        ni,nj=i+dx[dir],j+dy[dir]
                        # 갈 수 있는 칸 (물고기 있는 칸 or 빈 칸)
                        if 0<=ni<4 and 0<=nj<4 and not (ni==sx and nj==sy):
                            board[ni][nj][0],board[i][j][0]=board[i][j][0],board[ni][nj][0]
                            board[ni][nj][1],board[i][j][1]=dir,board[ni][nj][1]
                            flag = 1
                            break
                        # 갈 수 없는 칸 => 방향 45도 회전
                        dir=(dir+1)%8
                    if flag: break
            if flag: break

# 상어 이동
def moveShark(board,x,y):
    ableEat=[]
    d=board[x][y][1]

    for _ in range(3):
        nx,ny=x+dx[d],y+dy[d]
        if 0<=nx<4 and 0<=ny<4:
            if 1<=board[nx][ny][0]<=16:
                ableEat.append([nx,ny])
        else: break
        x,y=nx,ny
    return ableEat

def dfs(board,x,y,eatEnt):
    global result

    board = copy.deepcopy(board)
    fishNum=board[x][y][0]
    board[x][y][0]=-1

    # 모든 물고기 이동
    moveFishes(board,x,y)

    # 상어 이동, 먹을 수 있는 물고기 찾기
    ableEat=moveShark(board,x,y)

    result=max(result,eatEnt+fishNum)
    for ax,ay in ableEat:
        dfs(board,ax,ay,eatEnt+fishNum)

temp=[list(map(int, input().split())) for _ in range(4)]
board=[[None]*4 for _ in range(4)]      # (물고기 번호,방향) 저장
for i in range(4):
    for j in range(4):
        board[i][j]=[temp[i][j*2],temp[i][j*2+1]-1]

result=0
dfs(board,0,0,0)
print(result)