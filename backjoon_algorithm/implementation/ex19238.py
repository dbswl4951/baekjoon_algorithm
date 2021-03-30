#스타트 택시
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def getShorestDistance(x,y):
    q = deque()
    q.append([x, y])
    visited = [[-1] * (n + 1) for _ in range(n + 1)]
    visited[x][y]=0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 < nx <= n and 0 < ny <= n and board[nx][ny] == 0 and visited[nx][ny] ==-1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
    return visited

def bfs(ex,ey,x,y):
    q=deque()
    q.append([x,y])
    visited=[[-1]*(n+1) for _ in range(n+1)]
    visited[x][y]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<nx<=n and 0<ny<=n and board[nx][ny]==0 and visited[nx][ny]==-1:
                visited[nx][ny]=visited[x][y]+1
                if nx==ex and ny==ey: break
                q.append([nx,ny])
    if visited[ex][ey]!=-1:
        return visited[ex][ey]
    else:
        return -1

n,m,fuel=map(int,sys.stdin.readline().split())
board=[[0]*(n+1)]+[[0]+list(map(int,sys.stdin.readline().split())) for _ in range(n)]
x,y=map(int,sys.stdin.readline().split())
passengers=[list(map(int,sys.stdin.readline().split())) for _ in range(m)]

while passengers:
    p = []
    idx=0
    sx,sy,ex,ey=0,0,0,0

    # 가장 가까운 거리 승객 구함
    visited=getShorestDistance(x,y)
    for i,pas in enumerate(passengers):
        if visited[pas[0]][pas[1]]!=-1:
            p.append([i,pas[0],pas[1],pas[2],pas[3],visited[pas[0]][pas[1]]])
    if not p:
        print(-1)
        sys.exit(0)
    p.sort(key=lambda x:(x[5],x[1],x[2]))
    passenger=p[0]

    # 택시가 승객 태우러 감
    fuel-=passenger[5]
    if fuel<0:
        print(-1)
        sys.exit(0)
    x,y=passenger[1],passenger[2]
    board[x][y]=0

    # 승객을 목적지까지 이동
    distance=bfs(passenger[3],passenger[4],x,y)
    if distance==-1:
        print(-1)
        sys.exit(0)
    x,y=passenger[3],passenger[4]
    board[x][y]=0
    fuel-=distance
    if fuel<0:
        print(-1)
        sys.exit(0)
    fuel+=(2*distance)
    passengers.pop(passenger[0])
print(fuel)