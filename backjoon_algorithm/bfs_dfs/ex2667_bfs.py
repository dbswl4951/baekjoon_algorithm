#단지 번호 붙이기
'''
bfs
n을 y로 잘못 쓰거나 sort()를 안해주는등 이상한 실수를 함
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    global cnt
    q=deque()
    q.append([x,y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and city[nx][ny]==1:
                visited[nx][ny]=1
                q.append([nx,ny])
                cnt+=1

n=int(sys.stdin.readline().strip())
city=[]
for _ in range(n):
    city.append(list(map(int,sys.stdin.readline().strip())))
visited=[[0]*n for _ in range(n)]
result=[]
for i in range(n):
    for j in range(n):
        cnt = 1
        if city[i][j]==1 and visited[i][j]==0:
            bfs(i,j)
            result.append(cnt)
print(len(result))
result.sort()
for r in result:
    print(r)