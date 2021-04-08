#치즈
'''
공기에 2면 이상 노출 된 치즈를 찾는게 POINT!

1) 치즈 칸 : 치즈+1
 visited 방문 X, q에 (nx,ny) 삽입 X
2) 그 외
 visited 방문 O, q에 (nx,ny) 삽입
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    global result
    visited=[[0]*m for _ in range(n)] 
    visited[0][0]=1
    q=deque()
    q.append([0,0])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==0:
                    if paper[nx][ny]>=1:
                        paper[nx][ny]+=1
                    # 공기 칸만 방문 체크 해주고, q에 삽입
                    else:
                        visited[nx][ny]=1
                        q.append([nx,ny])

n,m=map(int,sys.stdin.readline().split())
paper=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
result=0
while True:
    bfs()
    check=0
    for i in range(n):
        for j in range(m):
            # 치즈가 2면 이상 노출 되어 있을 때
            if paper[i][j]>=3:
                paper[i][j]=0
                check=1
            # 한 면만 노출 되어 있는 치즈 다시 1로 갱신
            elif paper[i][j]==2:
                paper[i][j]=1
    # 녹일 치즈가 있으면 +1초
    if check: result+=1
    else: break
print(result)