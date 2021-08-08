#낚시왕
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,1,-1]

# 방향 반대로 바꾸기
def changeDir(dir):
    if dir==0: return 1
    elif dir==1: return 0
    elif dir==2: return 3
    else: return 2

# 땅과 가장 가까운 상어 잡기
def catchShark(y):
    global result

    for i in range(r):
        if board[i][y]:
            s,d,z=board[i][y][0]
            result+=z
            board[i][y]=[]
            sharks.remove([i,y,s,d,z])
            return

# 상어들 이동
def moveSharks():
    # 모든 상어 이동
    while sharks:
        x,y,speed,dir,size = sharks.popleft()
        if len(board[x][y])>1: board[x][y]=board[x][y][1:]
        else: board[x][y]=[]
        s=speed
        # speed만큼 상어 이동
        while s:
            nx,ny=x+dx[dir],y+dy[dir]
            if 0<=nx<r and 0<=ny<c:
                x,y=nx,ny
                s -= 1
            # 범위 밖이면 방향 반대로 바꾼 뒤 이동
            else:
                dir=changeDir(dir)
        board[x][y].append([speed,dir,size])

    # 한 칸에 상어가 여러마리인지 확인
    for i in range(r):
        for j in range(c):
            if board[i][j]:
                # 한 칸에 여러마리의 상어가 있다면
                if len(board[i][j])>1:
                    # 크기 순으로 정렬
                    board[i][j].sort(key=lambda x:-x[2])
                # 가장 크기 큰 애만 남도록 함
                board[i][j]=board[i][j][:1]
                sharks.append([i,j,board[i][j][0][0],board[i][j][0][1],board[i][j][0][2]])

r,c,m=map(int,sys.stdin.readline().split())
board=[[[] for _ in range(c)] for _ in range(r)]   # 상어의 속력, 방향, 크기 저장
sharks=deque()
for _ in range(m):
    x,y,s,d,z=map(int,sys.stdin.readline().split())
    sharks.append([x-1,y-1,s,d-1,z])
    board[x-1][y-1].append([s,d-1,z])
result=0
for i in range(c):  # i : 낚시꾼의 위치
    catchShark(i)
    moveSharks()
print(result)