#레이저 통신
import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    q.extend([[sx,sy,0],[sx,sy,1],[sx,sy,2],[sx,sy,3]])
    visited = [[[float('inf')]*4 for _ in range(w)] for _ in range(h)]
    visited[sx][sy] = [0,0,0,0]
    flag = 0

    while q:
        x,y,dir = q.popleft()

        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<h and 0<=ny<w and board[nx][ny]!='*':
                # 그 전의 거울 개수
                cnt = visited[x][y][dir]
                if flag and (0<=dir<=1 and 2<=i<=3) or (2<=dir<=3 and 0<=i<=1):
                    cnt += 1

                # 방문하지 않았거나, 현재 거울 개수가 더 최소면 갱신
                if visited[nx][ny][i]==-1 or visited[nx][ny][i]>cnt:
                    visited[nx][ny][i] = cnt
                    q.append([nx,ny,i])
        flag = 1
    return min(visited[ex][ey])

w,h = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(h)]
sx,sy,ex,ey = -1,-1,-1,-1
for i in range(h):
    for j in range(w):
        if board[i][j] == 'C' and sx==-1: sx,sy = i,j
        elif board[i][j] == 'C': ex,ey = i,j
print(bfs())