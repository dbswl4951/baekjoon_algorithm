#모노미노도미노 2

def targetGreen(a,b,c):
    # 1X1, 2X1 블록
    if a == 1 or a == 3:
        for i in range(1, 7):
            if i == 6 or green[i][c] != 0:
                green[i - 1][c] = 1
                if a == 1: break
                green[i - 2][c] = 1
                break
    # 1X2 블록
    elif a == 2:
        block = [c, c + 1]
        top = 6
        for by in block:
            for i in range(1, 6):
                if green[i][by] != 0:
                    top = min(top, i)
                    break
        green[top - 1][c], green[top - 1][c + 1] = 1, 1

def tagetBlue(a,b,c):
    # 1X1, 1X2 블록
    if a==1 or a==2:
        for i in range(1, 7):
            if i==6 or blue[i][3-b]!=0:
                blue[i-1][3-b] = 1
                if a==1: break
                blue[i-2][3-b] = 1
                break
    # 2X1 블록
    elif a==3:
        block = [3-b,2-b]
        top = 6
        for by in block:
            for i in range(1,6):
                if blue[i][by] != 0:
                    top = min(top, i)
                    break
        blue[top-1][3-b],blue[top-1][2-b] = 1,1

# 행 삭제 + 블럭 내리기
def checkRows(board):
    global result
    top,rowCnt = 5,0

    # 행 삭제
    for i in range(6):
        cnt = 0
        for j in range(4):
            if board[i][j] == 1: cnt+=1
        if cnt == 4:
            for j in range(4):
                board[i][j] = 0
            result += 1
            top = i
            rowCnt += 1

    # 블럭 내리기
    if rowCnt:
        for j in range(4):
            for i in range(top-1,-1,-1):
                if board[i][j] != 0:
                    board[i][j] = 0
                    board[i+rowCnt][j] = 1
    return board

# 0,1행 검사
def checkZeroOneRows(board):
    cnt = 0

    for i in range(0,2):
        for j in range(4):
            if board[i][j]!= 0:
                cnt += 1
                break
    if cnt:
        board = [[0]*4 for _ in range(cnt)] + board[:6-cnt][:]
    return board

n = int(input())
green,blue = [[0]*4 for _ in range(6)],[[0]*4 for _ in range(6)]
result,count = 0,0

for _ in range(n):
    a,b,c = map(int,input().split())
    # green
    targetGreen(a,b,c)
    green = checkRows(green)
    green = checkZeroOneRows(green)
    # blue
    tagetBlue(a,b,c)
    blue = checkRows(blue)
    blue = checkZeroOneRows(blue)

print(result)
for i in range(6):
    count += sum(green[i])
    count += sum(blue[i])
print(count)