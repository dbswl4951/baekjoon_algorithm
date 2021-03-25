#뱀
import sys
from collections import deque

#우하좌상
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def changeDirection(dir,v):
    # 왼쪽 회전
    if v=='L':
        dir=(dir-1)%4
    # 오른쪽 회전
    else:
        dir=(dir+1)%4
    return dir

def bfs():
    global time
    snake=deque([[1,1]])    # 뱀의 몸 저장
    q=deque()
    q.append([1,1])     # [머리x,머리y]
    dir=0   # 맨 처음에 오른쪽으로 이동 (0)

    while q:
        time += 1
        hx,hy=q.popleft()     # [머리x,머리y]
        # 머리를 현재 방향으로 이동
        nhx,nhy=hx+dx[dir],hy+dy[dir]
        if 0<nhx<=n and 0<nhy<=n:
            # 자기 몸에 부딪힐 경우 break
            if [nhx,nhy] in snake:
                break
            snake.append([nhx, nhy])
            # 움직인 방향에 사과가 있으면, 사과먹고 꼬리 그대로
            if board[nhx][nhy]==1:
                board[nhx][nhy]=0
            # 움직인 방향이 비어있다면, 꼬리 이동
            else:
                snake.popleft()
            q.append([nhx,nhy])

            # 90도 회전
            if directions and time==directions[0][0]:
                dir=changeDirection(dir,directions[0][1])
                directions.popleft()
        # 범위 벗어나면 break
        else: break
    return time

n=int(sys.stdin.readline().strip())
k=int(sys.stdin.readline().strip())
board=[[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a,b=map(int,sys.stdin.readline().split())
    # 사과가 있는 위치 1로 지정
    board[a][b]=1
l=int(sys.stdin.readline().strip())
directions=deque()
for _ in range(l):
    c,d=sys.stdin.readline().split()
    directions.append([int(c),d])
time=0
print(bfs())