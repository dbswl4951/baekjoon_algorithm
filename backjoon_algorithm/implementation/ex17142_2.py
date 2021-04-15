#연구소 3
import sys
from collections import deque
from itertools import combinations

dx=[1,-1,0,0]
dy=[0,0,-1,1]

# 바이러스 퍼트리기
def bfs(case):
    visited = [[-1] * n for _ in range(n)]
    q=deque()
    for c in case:
        q.append(c)
        visited[c[0]][c[1]]=0
    while q:
        qLen = len(q)
        while qLen:
            x,y=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<n and room[nx][ny]!=1 and visited[nx][ny]==-1:
                    visited[nx][ny]=visited[x][y]+1
                    q.append([nx,ny])
            qLen-=1
    for i in range(n):
        for j in range(n):
            if visited[i][j]==-1 and room[i][j]!=1: return -1
    time=0
    for i in range(n):
        for j in range(n):
            if room[i][j]!=2:
                time=max(time,visited[i][j])
    return time

n,m=map(int,sys.stdin.readline().split())
room=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
virus=deque()
for i in range(n):
    for j in range(n):
        if room[i][j]==2: virus.append([i,j])
result=int(1e9)
for case in combinations(virus,m):
    time=bfs(case)
    if time!=-1:
        result=min(result,time)
if result==int(1e9): print(-1)
else: print(result)