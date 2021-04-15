#욕심쟁이 판다
'''
1) 단순 bfs 사용 => 시간 초과
2) bfs + dp 사용 => 시간 초과
bfs는 들렸던 경로도 다시 가서 확인 하기 때문에 시간이 오래 걸리는 듯 하다
3) dfs + dp (top-down)
dp[x][y] : 가장 오래 살 수 있는 일 수
'''
import sys
sys.setrecursionlimit(10**6)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    # 방문 했던 곳은 바로 return해서 불필요한 연산 하지 않게 함
    if dp[x][y]: return dp[x][y]
    dp[x][y]=1
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n and forest[nx][ny]>forest[x][y]:
            dp[x][y]=max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y]

n=int(sys.stdin.readline().strip())
forest=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]
result=0
for i in range(n):
    for j in range(n):
        result=max(result,dfs(i,j))
print(result)


# bfs + dp 사용 => 시간 초과
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    global result
    q=deque()
    q.append([x,y])
    visited=[[0]*n for _ in range(n)]
    visited[x][y]=1
    rx,ry=x,y
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and forest[nx][ny]>forest[x][y]:
                visited[nx][ny]=visited[x][y]+1
                q.append([nx,ny])
                rx,ry=nx,ny
    result=max(result,visited[rx][ry])

n=int(sys.stdin.readline().strip())
forest=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
result=0
for i in range(n):
    for j in range(n):
        bfs(i,j)
print(result)
'''