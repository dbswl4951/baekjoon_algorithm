#상어 초등학교

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 자리 정하기
def setPosition(student):
    positionInfo = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                temp = [0,0,-i,-j]    # (좋아하는 학생 수, 빈 칸 수, x, y)
                for k in range(4):
                    ni,nj = i+dx[k],j+dy[k]
                    if 0<=ni<n and 0<=nj<n:
                        # 좋아하는 학생 수 세기
                        if board[ni][nj] in studentsDic[student]:
                            temp[0] += 1
                        # 빈 칸 개수 세기
                        if board[ni][nj] == 0:
                            temp[1] += 1
                positionInfo.append(temp)

    positionInfo.sort(reverse=True)
    board[-positionInfo[0][2]][-positionInfo[0][3]] = student

# 만족도 구하기
def getLikePer(student,x,y):
    cnt,per = 0,0

    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n and board[nx][ny] in studentsDic[student]:
            cnt += 1

    if cnt==1: per+=1
    elif cnt==2: per+=10
    elif cnt==3: per+=100
    elif cnt==4: per+=1000
    return per

n = int(input())
studentsDic,students = {},[]
board = [[0]*n for _ in range(n)]
for _ in range(n*n):
    temp = list(map(int,input().split()))
    students.append(temp[0])
    studentsDic[temp[0]] = temp[1:]

# 자리 정하기
for student in students:
    setPosition(student)
result = 0
# 만족도 구하기
for i in range(n):
    for j in range(n):
        result += getLikePer(board[i][j],i,j)
print(result)