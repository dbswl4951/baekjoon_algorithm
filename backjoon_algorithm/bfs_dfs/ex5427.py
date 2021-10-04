#불
import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    time = 0

    while True:
        sLen, fLen = len(q), len(fire)

        # 불 퍼트리기
        while fLen:
            x,y = fire.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0<=nx<h and 0<=ny<w and not fireVisited[nx][ny] and board[nx][ny]!='#':
                    board[nx][ny] = '*'
                    fireVisited[nx][ny] = 1
                    fire.append([nx,ny])
            fLen -= 1

        if sLen==0: break
        # 상근이 이동
        while sLen:
            x,y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0<=nx<h and 0<=ny<w:
                    if not visited[nx][ny] and board[nx][ny]!='*' and board[nx][ny]!='#':
                        visited[nx][ny] = 1
                        q.append([nx,ny])
                else:
                    return time + 1
            sLen -= 1
        time +=1
    return -1

t = int(sys.stdin.readline().strip())
for _ in range(t):
    w,h = map(int,sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(h)]
    fire,q = deque(),deque()
    fireVisited = [[0] * w for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                q.append([i,j])
                visited[i][j] = 1
            elif board[i][j] == '*':
                fire.append([i,j])
                fireVisited[i][j] = 1
    result = bfs()
    if result == -1: print('IMPOSSIBLE')
    else: print(result)