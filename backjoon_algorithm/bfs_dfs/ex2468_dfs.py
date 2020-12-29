#안전 영역
'''
예외처리는 다른 사람 풀이 참조 (35번째 줄)
'''
import sys
from collections import deque
sys.setrecursionlimit(100000)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,h):
    global visited
    q=deque()
    q.append([x,y])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and area[nx][ny]>h and visited[nx][ny]==0:
                visited[nx][ny]=1
                q.append([nx,ny])

n=int(input())
area=[]
for _ in range(n):
    area.append(list(map(int,sys.stdin.readline().split())))
result=0
for h in range(0,101):
    visited = [[0] * n for _ in range(n)]
    count=0
    for i in range(n):
        for j in range(n):
            if area[i][j]>h and visited[i][j]==0:
                visited[i][j] = 1
                bfs(i,j,h)
                count+=1
    result=max(result,count)
print(result)