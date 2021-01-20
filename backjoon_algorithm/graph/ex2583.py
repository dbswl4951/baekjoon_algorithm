#영역 구하기
'''
bfs

처음에 직사각형을 좌표를 list로 옮겨 채우는 과정에서 막혀서 다른 사람 코드 참조.
bfs 자체는 기본적인 bfs문제
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    count=1
    q=deque()
    q.append([x,y])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<m and 0<=ny<n and visited[nx][ny]==0 and board[nx][ny]==0:
                visited[nx][ny]=1
                q.append([nx,ny])
                count+=1
    return count

m,n,k=map(int,sys.stdin.readline().split()) #세로, 가로, 직사각형 수
board=[[0]*n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    for i in range(y1,y2):  #직사각형 표시 (상하 반전)
        for j in range(x1,x2):
            board[i][j]=1
visited=[[0]*n for _ in range(m)]
result=[]
for i in range(m):
    for j in range(n):
        if visited[i][j]==0 and board[i][j]==0:
            visited[i][j]=1
            result.append(bfs(i,j))
result.sort()
print(len(result))
for r in result:
    print(r,end=' ')