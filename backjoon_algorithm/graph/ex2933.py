#미네랄
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#미네랄 부수기
def breakMineral(h,d):
    y=-1  #부순 미네랄의 위치
    if d==1:    #왼쪽->오른쪽
        for i in range(c):
            if cave[h][i]=='x':
                cave[h][i]='.'
                y=i
                break
    else:   #오른쪽->왼쪽
        for i in range(c-1,-1,-1):
            if cave[h][i]=='x':
                cave[h][i]='.'
                y=i
                break
    for i in range(4):  #분리된 클러스터가 있는지 확인하기 위해, 부순 클리스터 상하좌우를 queue에 넣음
        nx,ny=h+dx[i],y+dy[i]
        if 0<=nx<r and 0<=ny<c and cave[nx][ny]=='x':
            dec.append([nx,ny])

#분리된 클러스터 구하기
def bfs(x,y):
    q=deque()
    q.append([x,y])
    fallList=[]     #떨어지는 클러스터들의 맨 아래 부분
    visited=[[0]*c for _ in range(r)]
    visited[x][y]=1
    while q:
        x,y=q.popleft()
        if x == r - 1:  # 바닥에 닿으면 종료
            return
        if cave[x + 1][y] == '.':   #클러스터의 아래칸이 .이면 떨어질 수 있는 클러스터의 맨 아래이므로 저장
            fallList.append([x, y])
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<r and 0<=ny<c and cave[nx][ny]=='x' and visited[nx][ny]==0:    #연결 된 모든 클러스터 확인
                visited[nx][ny]=1
                q.append([nx,ny])
    fall(visited,fallList)  #떨어져야 하는 클러스터를 떨어트림

#클러스터가 얼마나 떨어져야 하는지 확인 후, 클러스터를 및에서 부터 떨어트림
def fall(visited,fallList):
    h,flag=1,0  #h:떨어지는 높이, flag:떨어졌는지 아닌지 판단
    while True:
        for x,y in fallList:
            if x+h==r-1:    #h만큼 떨어져서 바닥에 도착하면
                flag=1
                break
            if cave[x+h+1][y]=='x' and visited[x+h+1][y]==0:    #떨어지는 곳에 미네랄이 있거나 떨어지는 클러스터에 연결된 부분이 아니라면
                flag=1
                break
        if flag: break  #클러스터가 하나라도 떨어졌다면 stop
        h+=1    #떨어지는 높이+1
    for i in range(r-2,-1,-1):
        for j in range(c):
            if cave[i][j]=='x' and visited[i][j]==1:    #떨어져야 할 클러스터 조각이라면
                cave[i][j]='.'  #원래 위치는 빈 칸으로
                cave[i+h][j]='x'    #h만큼 떨어짐

r,c=map(int,sys.stdin.readline().split())
cave=[]
for _ in range(r):
    cave.append(list(sys.stdin.readline().strip()))
n=int(sys.stdin.readline().strip())
height=deque(map(int,sys.stdin.readline().split()))
dec=deque()
d=1     #왼쪽부터 던지는지 오른쪽부터 던지는지 판별 (1:왼쪽, 2:오른쪽)
while height:
    h=height.popleft()
    h=r-h
    breakMineral(h,d)   #미네랄 부수기
    while dec:
        x,y=dec.popleft()
        bfs(x,y)    #분리된 클러스터 구하기
    d*=-1   #왼쪽, 오른쪽 방향 바꿔줌
for i in range(r):
    for j in range(c):
        print(cave[i][j],end='')
    print()