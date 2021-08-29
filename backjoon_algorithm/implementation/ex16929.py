#Two Dots
import sys

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,color,cnt,sx,sy):
    global result

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<m and board[nx][ny]==color:
            if not visited[nx][ny]:
                visited[x][y] = 1
                dfs(nx,ny,color,cnt+1,sx,sy)
                visited[x][y] = 0
            else:
                if nx==sx and ny==sy and cnt>=4:
                    result=1
                    return
        if result: return

n,m = map(int,sys.stdin.readline().split())
board=[list(sys.stdin.readline().strip()) for _ in range(n)]
visited =[[0]*m for _ in range(n)]
result=0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j]=1
            dfs(i,j,board[i][j],1,i,j)
            if result:
                print('Yes')
                sys.exit(0)
print('No')