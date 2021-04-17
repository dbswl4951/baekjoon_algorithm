#청소년 상어
'''
dfs + 백트래킹 문제

1. 현재 상어 위치에 있는 물고기를 먹기
2. 모든 물고기를 이동시킴
3. 상어가 먹을 수 있는 물고기 파악
4. 3번의 모든 경우에 대해 dfs 탐색

백트래킹에 너무 약한 것 같다ㅜ.ㅜ
'''
import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 상어 이동 => 먹을 수 있는 모든 물고기 저장
def moveShark(board,sx,sy):
    ableEat=[]
    dir=board[sx][sy][1]
    # 최대 3번 이동 가능
    for i in range(3):
        nx,ny=sx+dx[dir],sy+dy[dir]
        # 범위내에 있고, 물고기가 있으면 이동 가능
        if 0<=nx<4 and 0<=ny<4 and 1<=board[nx][ny][0]<=16:
            ableEat.append([nx,ny])
        sx,sy=nx,ny
    return ableEat

# 물고기 이동
def moveFish(board,sx,sy):
    # 특정 번호의 물고기 위치 찾기
    for num in range(1,17):
        flag = 0
        for i in range(4):
            for j in range(4):
                if board[i][j][0]==num:
                    dir=board[i][j][1]
                    # 회전 횟수 최대 8번
                    for k in range(8):
                        ni,nj=i+dx[dir],j+dy[dir]
                        # 범위내에 있고, 상어가 없는 곳이면 물고기 이동
                        if 0<=ni<4 and 0<=nj<4 and not (sx==ni and sy==nj):
                            board[ni][nj][0],board[i][j][0]=board[i][j][0],board[ni][nj][0]
                            board[ni][nj][1],board[i][j][1]=dir,board[ni][nj][1]
                            flag=1
                            break
                        dir=(dir+1)%8
                    if flag: break
            if flag: break

# 먹을 수 있는 물고기에 대해 전체 탐색
def dfs(board,sx,sy,total):
    global result
    board=copy.deepcopy(board)
    # (sx,sy)위치의 물고기 먹기
    fishNum=board[sx][sy][0]
    board[sx][sy][0]=-1

    # 물고기 이동
    moveFish(board,sx,sy)
    # 상어 이동 => 먹을 수 있는 모든 물고기 저장
    ableEat=moveShark(board,sx,sy)

    # 먹을 수 있는 물고기에 대해 전체 탐색
    result=max(result,total+fishNum)
    for fx,fy in ableEat:
        dfs(board,fx,fy,total+fishNum)

temp=[list(map(int, input().split())) for _ in range(4)]
board=[[None]*4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        board[i][j]=[temp[i][j*2],temp[i][j*2+1]-1]

result=0
dfs(board,0,0,0)
print(result)