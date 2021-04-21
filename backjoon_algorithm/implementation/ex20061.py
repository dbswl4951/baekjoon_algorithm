#모노미노도미노 2

# 블럭 파란 보드로 이동 후 놓기
def moveToBlueBoard(block):
    row,col=4,6
    t,x,y=block

    # 1X1 블럭
    if t==1:
        for i in range(1,col):
            if blueBoard[x][i]:
                blueBoard[x][i-1]=1
                break
            if i==col-1: blueBoard[x][i]=1
    # 가로 모양 블럭
    elif t==2:
        for i in range(2,col):
            if blueBoard[x][i]:
                blueBoard[x][i-1]=1
                blueBoard[x][i-2]=1
                break
            if i == col - 1:
                blueBoard[x][i] = 1
                blueBoard[x][i-1] = 1
    # 세로 모양 블럭
    else:
        for i in range(1,col):
            if blueBoard[x][i] or blueBoard[x+1][i]:
                blueBoard[x][i-1]=1
                blueBoard[x+1][i-1]=1
                break
            if i == col - 1:
                blueBoard[x][i] = 1
                blueBoard[x + 1][i] = 1

# 블럭 초록 보드로 이동 후 놓기
def moveToGreenBoard(block):
    row,col=6,4
    t, x, y = block

    # 1X1 블럭
    if t == 1:
        for i in range(1,row):
            if greenBoard[i][y]:
                greenBoard[i-1][y]=1
                break
            if i == row - 1: greenBoard[i][y] = 1
    # 가로 모양 블럭
    elif t == 2:
        for i in range(1,row):
            if greenBoard[i][y] or greenBoard[i][y+1]:
                greenBoard[i-1][y] = 1
                greenBoard[i-1][y+1] = 1
                break
            if i==row-1:
                greenBoard[i][y]=1
                greenBoard[i][y+1] = 1
    # 세로 모양 블럭
    else:
        for i in range(2,row):
            if greenBoard[i][y]:
                greenBoard[i-1][y] = 1
                greenBoard[i-2][y] = 1
                break
            if i==row-1:
                greenBoard[i][y]=1
                greenBoard[i-1][y]=1

# 행 또는 열이 가득 찼는지 확인, 점수 증가, 블럭 삭제
def checkFull(board):
    global score
    delete=[]   # 삭제 가능 한 행/열 인덱스 저장
    for i in range(6):
        # 블럭 한 줄이 가득 참
        if sum(board[i])==4:
            score+=1
            delete.append(i)

    delete.sort()
    for d in delete:
        # 블럭 삭제
        for j in range(4):
            board[d][j] = 0
        for i in range(d-1,0,-1):
            for j in range(4):
                # 블럭 내리기
                if board[i][j]==1:
                    board[i+1][j]=1
                    board[i][j]=0

# 0,1 열/행에 블럭 있는지 검사, 삭제
def checkZeroOne(board):
    cnt=0
    for i in range(2):
        if sum(board[i])!=0:
            cnt+=1
    board=[[0,0,0,0] for _ in range(cnt)]+board[:6-cnt]
    return board


n=int(input().strip())
block=[list(map(int,input().split())) for _ in range(n)]    # (t,x,y)
blueBoard=[[0]*6 for _ in range(4)]
greenBoard=[[0]*4 for _ in range(6)]

score=0
# 블럭 놓기 시작
for i in range(n):
    # 파란색 보드에 블럭 놓기
    moveToBlueBoard(block[i])
    # 초록색 보드에 블럭 놓기
    moveToGreenBoard(block[i])

    # 초록 보드 행 가득 찼는지 확인 + 점수 증가 + 삭제
    checkFull(greenBoard)
    # 파란 보드 행 가득 찼는지 확인 + 점수 증가 + 삭제
    blueBoard=list(map(list,zip(*blueBoard)))
    checkFull(blueBoard)
    blueBoard=list(map(list,zip(*blueBoard)))

    # 초록 보드 0행, 1행 검사
    greenBoard=checkZeroOne(greenBoard)
    # 파란 보드 0열, 1열 검사
    blueBoard = list(map(list, zip(*blueBoard)))
    blueBoard=checkZeroOne(blueBoard)
    blueBoard = list(map(list, zip(*blueBoard)))

print(score)
blockSum=0
for bb in blueBoard:
    blockSum+=sum(bb)
for gb in greenBoard:
    blockSum+=sum(gb)
print(blockSum)