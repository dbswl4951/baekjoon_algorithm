#낚시왕

dx=[-1,1,0,0]
dy=[0,0,1,-1]

# 방향 반대로 바꾸기
def changeDir(dir):
    if dir==0: return 1
    elif dir==1: return 0
    elif dir==2: return 3
    else: return 2

# 상어 잡기
def huntShark(col):
    global result
    for i in range(r):
        if board[i][col]:
            size=board[i][col][0]
            board[i][col]=[]
            for j in range(m):
                if sharks[j][4]==size:
                    result+=size
                    sharks[j]=[0,0,0,0,0]
                    break
            break

# 상어 이동
def moveShark(i,shark):
    x,y,s,d,z=shark
    nx,ny,ns=x,y,s
    while ns:
        nx,ny=nx+dx[d],ny+dy[d]
        if not 0<=nx<r or not 0<=ny<c:
            d=changeDir(d)
            ns+=1
        else: ns-=1
    size=board[x][y][0]
    board[x][y].remove(size)
    board[nx][ny].append(size)
    sharks[i]=[nx,ny,s,d,z]

# 한 칸에 여러마리 상어가 있는지 체크 + 여러마리면 큰 상어만 남기고 삭제
def checkSharksAndEat():
    for i in range(r):
        for j in range(c):
            if len(board[i][j])>1:
                maxSize=max(board[i][j])
                idx=0
                while len(board[i][j])>1:
                    if board[i][j][idx]!=maxSize:
                        size=board[i][j][idx]
                        board[i][j].pop(idx)
                        for k in range(len(sharks)):
                            if sharks[k][4]==size:
                                sharks[k]=[0,0,0,0,0]
                    else: idx+=1

r,c,m=map(int,input().split())
board=[[[] for _ in range(c)] for _ in range(r)]     # (x,y)에 있는 상어의 크기 저장
sharks=[]
for _ in range(m):
    x,y,s,d,z=map(int,input().split())
    sharks.append([x-1,y-1,s,d-1,z])
    board[x-1][y-1].append(z)

result=0
for i in range(c):
    # 낚시왕이 상어 잡음
    huntShark(i)
    # 모든 상어 이동
    for j in range(m):
        if sharks[j][4]!=0:
            moveShark(j,sharks[j])
    # 한 칸에 여러 마리 상어 있으면 큰 상어만 남기기
    checkSharksAndEat()
print(result)