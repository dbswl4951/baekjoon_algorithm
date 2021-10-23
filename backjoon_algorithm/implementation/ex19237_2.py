#어른 상어

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 시간 -1 & 냄새 뿌리기
def spreadSmells():
    # 시간 -1
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                board[i][j][1] -= 1
                if board[i][j][1] == 0:
                    board[i][j] = []

    # 냄새 뿌리기
    for i in range(n):
        for j in range(n):
            if sharks[i][j]:
                board[i][j] = [sharks[i][j][0][0],k]

# 상어 이동
def moveSharks():
    global mCnt
    check = [0]*(m+1)

    for i in range(n):
        for j in range(n):
            if sharks[i][j] and not check[sharks[i][j][0][0]]:
                sNum,sd = sharks[i][j].pop()
                check[sNum],flag = 1,0

                # 빈 칸 확인
                for k in range(4):
                    nsd = prior[sNum-1][sd][k]
                    ni,nj = i+dx[nsd],j+dy[nsd]
                    if 0<=ni<n and 0<=nj<n:
                        # 빈 칸
                        if not board[ni][nj]:
                            sharks[ni][nj].append([sNum, nsd])
                            flag = 1
                            break
                # 자기 자신의 냄새 칸 확인
                if not flag:
                    for k in range(4):
                        nsd = prior[sNum-1][sd][k]
                        ni,nj = i+dx[nsd],j+dy[nsd]
                        if 0<=ni<n and 0<=nj<n:
                            if board[ni][nj][0] == sNum:
                                sharks[ni][nj].append([sNum, nsd])
                                break

    # 한 칸에 여러마리 있는지 check
    for i in range(n):
        for j in range(n):
            if len(sharks[i][j])>1:
                mCnt -= (len(sharks[i][j]) - 1)
                sharks[i][j].sort()
                sharks[i][j] = [sharks[i][j][0]]

n,m,k = map(int,input().split())
sharks = [[[] for _ in range(n)] for _ in range(n)] # (x,y)위치에 있는 [상어 번호, 방향] 저장
board = [[[] for _ in range(n)] for _ in range(n)]  # [상어번호, 남은시간] 저장
temp = [list(map(int,input().split())) for _ in range(n)]
dir = list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if temp[i][j]!=0:
            sharks[i][j].append([temp[i][j],dir[temp[i][j]-1]-1])
prior = [[] for _ in range(m)]
for i in range(m*4):
    a,b,c,d = map(int,input().split())
    prior[i//4].append([a-1,b-1,c-1,d-1])
mCnt,result = m,0

while result<1001:
    # 시간 -1 & 냄새 뿌리기
    spreadSmells()
    # 상어 이동
    moveSharks()
    result += 1
    if mCnt == 1: break

if result==1001: print(-1)
else: print(result)