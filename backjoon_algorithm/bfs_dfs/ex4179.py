#불!
'''
BFS 2번 적용 시키는 문제
1. 지훈이 이동시키기
2. 불 퍼트리기

1차시도 : 메모리 초과
힌트 보고 불 태우는 과정 (burn) 함수에도 visited를 적용 시켜서 탐색했더니 맞음!!
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def burn():     #불 확산 시키기
    global fire,danger,fVisited
    for x,y in fire:
        fVisited[x][y]=1
    danger.clear()
    fireLen=len(fire)
    while fireLen > 0:
        x, y = fire.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<r and 0<=ny<c and maze[nx][ny]!='#' and fVisited[nx][ny]==0:
                if maze[nx][ny] == 'J' and [nx,ny] not in danger:  # 불이 지훈이를 만나면 실패
                    danger.append([nx,ny])
                fVisited[nx][ny]=1
                maze[nx][ny]='F'
                fire.append([nx,ny])
        fireLen-=1

def bfs(x,y):  #지훈이 이동
    global q,danger
    visited = [[0] * c for _ in range(r)]
    visited[x][y]=1
    q.append([x,y])
    while q:
        qLen = len(q)
        while qLen>0:
            x,y=q.popleft()
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if [x,y] not in danger and (nx==-1 or nx==r or ny==-1 or ny==c):
                    print(visited[x][y])
                    return
                if 0<=nx<r and 0<=ny<c and maze[nx][ny]=='.' and visited[nx][ny]==0:
                    visited[nx][ny]=visited[x][y]+1
                    q.append([nx,ny])
                    maze[nx][ny]='J'
                    maze[x][y]='.'
            qLen-=1
        burn()
    print("IMPOSSIBLE")
    return

r,c=map(int,sys.stdin.readline().split())
maze=[]
for _ in range(r):
    maze.append(list(sys.stdin.readline().strip()))
fire,danger=deque(),deque()
for i in range(r):  #지훈이의 초기 위치, 불의 위치 저장
    for j in range(c):
        if maze[i][j]=='J':
            startX,startY=i,j
        if maze[i][j]=='F':
            fire.append([i,j])
fVisited = [[0] * c for _ in range(r)]
q=deque()
bfs(startX,startY)