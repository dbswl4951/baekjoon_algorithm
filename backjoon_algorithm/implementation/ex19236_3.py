#청소년 상어
import copy

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

# 물고기 이동
def moveFishs(board,sx,sy):
    for k in range(1,17):
        flag = 0
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == k:
                    d = board[i][j][1]
                    for _ in range(9):
                        ni,nj = i+dx[d],j+dy[d]
                        if not 0<=ni<4 or not 0<=nj<4 or (ni==sx and nj==sy):
                            d = (d+1)%8
                        else:
                            board[i][j][1] = d
                            board[i][j],board[ni][nj] = board[ni][nj], board[i][j]
                            flag=1
                            break
                if flag: break
            if flag: break

# 상어가 먹을 수 있는 물고기 탐색
def getAble(board,sx,sy,d):
    ableEat = []

    for _ in range(3):
        nx,ny = sx+dx[d],sy+dy[d]
        if 0<=nx<4 and 0<=ny<4 and 1<=board[nx][ny][0]<=16:
            ableEat.append([nx,ny])
        sx,sy = nx,ny
    return ableEat

# 물고기 이동 + 상어 이동 + 먹기
def dfs(board,sx,sy,eat):
    global result

    # 한 흐름마다 동일한 board를 가지고 계산해야 함
    # copy를 안해주면, dfs 끝까지 간 후, 다시 돌아왔을 때 board는 변형되어 있음
    board = copy.deepcopy(board)
    num,d = board[sx][sy]
    board[sx][sy] = [-1,-1]

    # 물고기 이동
    moveFishs(board,sx,sy)
    # 상어가 먹을 수 있는 물고기 탐색
    ableEat = getAble(board,sx,sy,d)

    result = max(result,eat+num)
    for ax,ay in ableEat:
        dfs(board,ax,ay,eat+num)

board = [[[] for _ in range(4)] for _ in range(4)]
for i in range(4):
    temp = list(map(int,input().split()))
    for j in range(0,8,2):
        board[i][j//2].append(temp[j])
        board[i][j // 2].append(temp[j+1]-1)
result = 0
dfs(board,0,0,0)
print(result)