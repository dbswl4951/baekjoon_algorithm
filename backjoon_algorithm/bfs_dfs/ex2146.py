#다리 만들기
'''
bfs를 두번 쓰는 문제

1. 각각의 섬에 번호를 붙인다
2. 1,2,3...섬을 각각 돌면서 bfs 실행하면서 다른 번호의 섬을 만날 때 까지 visited 리스트(거리)의 값을 누적 시킨다.
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#섬에 번호 붙이기
def labeling(x,y,num):
    labelBoard[x][y] =num
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and labelBoard[nx][ny]== 0 and board[nx][ny]==1:
                q.append([nx,ny])
                labelBoard[nx][ny]=num

#각각의 num번 섬의 크기를 키워서 다른 섬과 만나는지 확인
def makeBridge(num):
    global visited
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny]==1 and labelBoard[nx][ny]!=num:    #다른 섬과 만나면
                    return visited[x][y]-1
                if board[nx][ny]==0 and visited[nx][ny]==0:  #바다라면 다리 놓기
                    visited[nx][ny]=visited[x][y]+1
                    q.append([nx,ny])

n=int(sys.stdin.readline().strip())
board=[]
for _ in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))
labelBoard=[[0]*n for _ in range(n)]
num=1
#섬에 라벨 붙이기
for i in range(n):
    for j in range(n):
        if labelBoard[i][j]==0 and board[i][j]==1:
            labeling(i,j,num)
            num += 1
reuslt=int(1e9)
#각각의 섬의 크기를 키워서 다른 섬과 만나는지 확인
for i in range(1,num):
    q = deque()
    visited = [[0] * n for _ in range(n)]
    #각각의 섬마다 좌표 모두 큐에 삽입 후, bfs실행
    for j in range(n):
        for k in range(n):
            if board[j][k]==1 and labelBoard[j][k]==i:
                q.append([j,k])
                visited[j][k]=1
    reuslt=min(reuslt,makeBridge(i))
print(reuslt)