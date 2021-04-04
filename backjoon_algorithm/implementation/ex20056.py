#마법사 상어와 파이어볼
import sys
from collections import deque

directions=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# 1번 과정 : 모든 파이어볼 이동 시킴
def moveFireball():
    fLen=len(fireball)
    temp = []
    for _ in range(fLen):
        x, y = fireball.popleft()
        # 한 칸에 있는 모든 파이어볼 이동 시키기
        for _ in range(len(board[x][y])):
            m, s, d = board[x][y].popleft()
            nx,ny=x,y
            # s 만큼 d 방향으로 이동
            for _ in range(s):
                nx, ny = nx + directions[d][0], ny + directions[d][1]
                if 0 <= nx < n and 0 <= ny < n:
                    continue
                # 범위 벗어 난 경우, 연결 된 부분으로 이동
                else:
                    if nx < 0:
                        nx = n - 1
                    elif nx >= n:
                        nx = 0
                    if ny < 0:
                        ny = n - 1
                    elif ny >= n:
                        ny = 0
            # 다음 탐색 할 파이어볼 위치 저장
            fireball.append([nx,ny])
            # 이동 시켜야 할 파이어볼 저장
            temp.append([nx,ny,m,s,d])
    # 파이어볼 한번에 다 이동
    for x, y, m, s, d in temp:
        board[x][y].append([m, s, d])

# 2번 과정 : 2개 이상인 파이어볼 합치고, 4개로 나누기
def divideFireball():
    for i in range(n):
        for j in range(n):
            # 파이어볼이 2개 이상인 칸이라면
            if len(board[i][j])>1:
                dir=[]
                nm,ns=0,0
                for m,s,d in board[i][j]:
                    nm+=m
                    ns+=s
                    dir.append(d)
                nm//=5
                ns//=len(board[i][j])
                # 원래 자리에 있던 파이어볼 없애기
                board[i][j]=deque()
                if nm == 0: continue
                if check(dir):
                    for k in range(0,7,2):
                        board[i][j].append([nm,ns,k])
                else:
                    for k in range(1, 8, 2):
                        board[i][j].append([nm,ns,k])

# 방향이 모두 짝수, 홀수 인지 판별
def check(dir):
    c=dir[0]%2
    for i in range(1,len(dir)):
        if dir[i]%2!=c:
            return False    # 방향이 홀수, 짝수 제각각
    return True # 방향이 모두 홀수이거나 짝수

n,m,k=map(int,sys.stdin.readline().split())
fireball=deque()    # 파이어볼 (x,y) 좌표 저장
board=[[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,m,s,d=map(int,sys.stdin.readline().split())
    fireball.append([x-1,y-1])
    board[x-1][y-1].append([m,s,d])

for _ in range(k):
    moveFireball()
    divideFireball()
result=0
for i in range(n):
    for j in range(n):
        if board[i][j]:
            for k in board[i][j]:
                result+=k[0]
print(result)
