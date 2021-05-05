#벽부수고 이동하기
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    q=deque()
    q.append([0,0,1])   # (x,y,벽 뚫기 가능 여부 (0:불가능, 1:가능))
    # visited[x][y] = [ 벽을 뚫었을 때 최단 거리, 벽을 뚫지 않았을 때 최단 거리 ]
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
    visited[0][0][1]=1

    while q:
        x,y,z=q.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y][z]

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <=nx<n and 0<=ny<m:
                # 벽을 만남 + 벽 뚫기 가능 => 벽 뚫기
                if board[nx][ny]==1 and z==1:
                    visited[nx][ny][0]=visited[x][y][1]+1
                    q.append([nx,ny,0])
                # 빈 칸 만남 + 아직 방문 안한 경우
                elif board[nx][ny]==0 and visited[nx][ny][z]==0:
                    visited[nx][ny][z]=visited[x][y][z]+1
                    q.append([nx,ny,z])
    return -1

n,m=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
print(bfs())


# 1차 시도 (dfs+백트레킹)
# 메모리 초과
'''
sys.setrecursionlimit(10**6)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,broke,cnt):
    global result

    if cnt>result: return
    if x==n-1 and y==m-1:
        result=min(result,cnt)
        return

    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny] = 1
            # 벽 부실수 있으면 부숨
            if board[nx][ny]==1 and broke==0:
                dfs(nx,ny,1,cnt+1)
            elif board[nx][ny]==0:
                dfs(nx,ny,broke,cnt+1)
            visited[nx][ny]=0

n,m=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
visited[0][0]=1
result=int(1e9)
dfs(0,0,0,1)
if result==int(1e9): print(-1)
else: print(result)
'''