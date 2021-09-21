#성곽
import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 깰 수 있는 벽 반환
def breakWall(x,y):
    able = []

    if x==0:
        if y==0:
            for i in range(2):
                if board[x][y][i]=='1':
                    able.append(i)
        elif y==m-1:
            for i in range(4):
                if i==1 or i==2: continue
                if board[x][y][i]=='1':
                    able.append(i)
        else:
            for i in range(4):
                if i==2: continue
                if board[x][y][i] == '1':
                    able.append(i)
    elif x==n-1:
        if y==0:
            for i in range(1,3):
                if board[x][y][i] == '1':
                    able.append(i)
        elif y==m-1:
            for i in range(2,4):
                if board[x][y][i]=='1':
                    able.append(i)
        else:
            for i in range(1,4):
                if board[x][y][i] == '1':
                    able.append(i)
    else:
        if y==0:
            for i in range(3):
                if board[x][y][i] == '1':
                    able.append(i)
        elif y==m-1:
            for i in range(4):
                if i==1: continue
                if board[x][y][i]=='1':
                    able.append(i)
        else:
            for i in range(4):
                if board[x][y][i] == '1':
                    able.append(i)
    return able

def bfs(i,j,visited):
    global roomArea
    q = deque()
    q.append([i,j])
    visited[i][j]=1
    count = 1

    while q:
        x,y=q.popleft()
        idx,cnt=len(board[x][y]),0

        while idx:
            if board[x][y][idx-1] == '0':
                if cnt==0:
                    nx,ny = x+dx[2],y+dy[2]
                elif cnt==1:
                    nx,ny = x+dx[0],y+dy[0]
                elif cnt==2:
                    nx, ny = x + dx[3], y + dy[3]
                else:
                    nx, ny = x + dx[1], y + dy[1]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                    q.append([nx,ny])
                    count+=1
                    visited[nx][ny]=1
            idx -= 1
            cnt += 1
    roomArea = max(roomArea,count)

m,n = map(int,sys.stdin.readline().split())
board = [['']*m for _ in range(n)]
for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    for j in range(m):
        twoNum = bin(temp[j])[2:]
        twoNum = '0'*(4-len(twoNum))+twoNum
        board[i][j]=twoNum

visited1 = [[0]*m for _ in range(n)]
roomCount,roomArea = 0,0
for i in range(n):
    for j in range(m):
        if not visited1[i][j]:
            roomCount+=1
            bfs(i,j,visited1)
print(roomCount)
print(roomArea)

# 벽 하나씩 제거해보기
for i in range(n):
    for j in range(m):
        wall = breakWall(i,j)
        origin = board[i][j]
        for w in wall:
            visited2 = [[0] * m for _ in range(n)]
            board[i][j] = origin[:w]+'0'+origin[w+1:]
            visited2[i][j]=1
            bfs(i,j,visited2)
            board[i][j] = origin
print(roomArea)