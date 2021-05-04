#상어 초등학교
'''
2021 삼성 상반기 오전 문제
'''

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 학생 자리 배치
def getPosition(student):
    priority=student[1:]
    x,y,priCnt,empCnt=-1,-1,-1,-1

    for i in range(n):
        for j in range(n):
            if board[i][j]==0:
                pCnt,eCnt=0,0
                for k in range(4):
                    ni,nj=i+dx[k],j+dy[k]
                    if 0<=ni<n and 0<=nj<n:
                        if board[ni][nj]==0: eCnt+=1
                        elif board[ni][nj] in priority: pCnt+=1

                # 선호 학생이 더 많이 있거나, 선호 학생 수가 같으면 빈 칸이 더 많은 곳으로 갱신
                if priCnt<pCnt or (priCnt==pCnt and empCnt<eCnt):
                    x,y,priCnt,empCnt=i,j,pCnt,eCnt

    board[x][y]=student[0]

# 학생 만족도 구하기
def getSatisfaction(student):
    global result
    sNum=student[0]
    priority=student[1:]
    sCnt = 0  # 인접한 학생 수

    for i in range(n):
        for j in range(n):
            if board[i][j]==sNum:
                for k in range(4):
                    ni,nj=i+dx[k],j+dy[k]
                    if 0 <= ni < n and 0 <= nj < n and board[ni][nj] in priority:
                        sCnt+=1

    if sCnt==1: result+=1
    elif sCnt==2: result+=10
    elif sCnt==3: result+=100
    elif sCnt==4: result+=1000

n=int(input().strip())
board=[[0]*n for _ in range(n)]
students=[list(map(int,input().split())) for _ in range(n*n)]
board[1][1]=students[0][0]

# 학생 자리 배치
for i in range(1,n*n):
    getPosition(students[i])

result=0
# 학생 만족도 구하기
for i in range(n*n):
    getSatisfaction(students[i])
print(result)