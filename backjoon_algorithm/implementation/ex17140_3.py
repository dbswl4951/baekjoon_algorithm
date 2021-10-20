#이차원 배열과 연산
from collections import Counter

# RC 연산
def RC(board):
    temp,n,m = [],len(board),0
    for i in range(n):
        counter = list(Counter(board[i]).items())
        counter.sort(key=lambda x: (x[1], x[0]))
        cnt = 0
        for j in range(len(counter)):
            if counter[j][0]!=0:
                temp.append(counter[j])
                cnt +=1
        m = max(m,cnt)
        temp.append((-1,-1))

    m *= 2
    if m>100: m=100
    newBoard = [[0]*m for _ in range(n)]

    x,y = 0,0
    for tx,ty in temp:
        if tx!=-1:
            newBoard[x][y] = tx
            newBoard[x][y+1] = ty
            y += 2
        else:
            x += 1
            y = 0
    return newBoard

r,c,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(3)]
result = 0

while result<=100:
    if r-1<len(board) and c-1<len(board[0]) and board[r - 1][c - 1] == k: break

    # R 연산
    if len(board) >= len(board[0]):
        board = RC(board)
    # C 연산
    else:
        # transpose
        board = RC(list(map(list,zip(*board))))
        board = list(map(list,zip(*board)))
    result += 1
if result>100: print(-1)
else: print(result)