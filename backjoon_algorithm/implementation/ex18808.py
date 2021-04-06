#스티커 붙이기
import sys,copy

# 노트북에 스티커 붙일 수 있는지 체크
def check(x,y):
    for i in range(r):
        for j in range(c):
            if board[x+i][y+j]==1 and sticker[i][j]==1:
                return 0
    for i in range(r):
        for j in range(c):
            if sticker[i][j]==1:
                board[x+i][y+j]=1
    return 1

# 스티커 회전, 이동
def move(rotate):
    global sticker,r,c
    # 시계 방향으로 90도 회전
    if rotate:
        temp=[]
        for l in zip(*sticker):
            temp.append(list(reversed(l)))
        sticker=copy.deepcopy(temp)
        r,c=len(sticker),len(sticker[0])

    # 이동 시킬 수 있는 x 범위 구하기
    for i in range(n):
        if n-i<r: break
        for j in range(m):
            if m-j<c: break
            # 스티커 붙일 수 있으면 1 return
            if check(i,j): return 1
    # 스티커 붙일 수 없음
    return 0

n,m,k=map(int,sys.stdin.readline().split())
board=[[0]*m for _ in range(n)]     # 노트북
for _ in range(k):
    r,c=map(int,sys.stdin.readline().split())
    sticker=[list(map(int,sys.stdin.readline().split())) for _ in range(r)]
    # 맨 처음은 회전하지 않고 수행
    flag=move(0)
    for _ in range(3):
        # 스티커 붙일 수 없다면 회전 실행 (최대 3번)
        if flag==0:
            flag=move(1)

result=0
for b in board:
    result+=sum(b)
print(result)