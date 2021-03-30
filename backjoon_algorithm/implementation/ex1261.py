#알고스팟
'''
[ 새로 알게 된 점 ]
deque()의 appendleft()
: 큐의 맨 앞에 원소 추가

벽을 부수는 비용 : 1, 빈 칸 비용 : 0이므로
적은 비용 (빈 칸일때) 먼저 탐색 후, 큰 비용 (벽) 탐색
'''
import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,-1,1]

def bfs():
    visited=[[-1]*n for _ in range(m)]
    visited[0][0]=0
    q=deque()
    q.append([0,0])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<m and 0<=ny<n and visited[nx][ny]==-1:
                #빈 칸
                if maze[nx][ny]==0:
                    visited[nx][ny]=visited[x][y]
                    #빈 칸일때의 탐색을 더 우선시 (큐의 맨 앞에 삽입)
                    q.appendleft([nx,ny])
                #벽
                else:
                    visited[nx][ny]=visited[x][y]+1
                    #벽일때는 큐 뒷편에 삽입
                    q.append([nx,ny])
    print(visited[m-1][n-1])

n,m=map(int,sys.stdin.readline().split())
maze=[list(map(int,sys.stdin.readline().strip())) for _ in range(m)]
bfs()