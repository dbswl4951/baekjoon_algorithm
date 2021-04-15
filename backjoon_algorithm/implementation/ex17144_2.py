#미세먼지 안녕
'''
포인트는 확산 된 먼지를 바로바로 갱신하지 않고, 다 계산 후 갱신하는 것
'''
import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,-1,1]

# 미세먼지 확산 시키기
def spread(room):
    spreadRoom=[[0]*c for _ in range(r)]  # 확산 된 먼지를 저장
    while dust:
        x,y=dust.popleft()
        sd=room[x][y]//5
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<r and 0<=ny<c and room[nx][ny]!=-1:
                room[x][y]-=sd
                spreadRoom[nx][ny]+=sd
    # 확산된 미세먼지 + 확산되고 남은 미세먼지
    for i in range(r):
        for j in range(c):
            room[i][j]=room[i][j]+spreadRoom[i][j]
    return room

# 공기청정기 작동
def airFrash():
    ax1,ax2=frash[0],frash[1]   # 공기청정기 위쪽 x좌표, 아래쪽 x좌표
    # 위쪽 공기 청정기 작동
    moveDown(ax1-1,0,0)
    moveLeft(0)
    moveUp(1,ax1+1,c-1)
    moveRight(ax1)
    # 아래 공기 청정기 작동
    moveUp(ax2+2,r,0)
    moveLeft(r-1)
    moveDown(r-1,ax2,c-1)
    moveRight(ax2)

# 왼쪽 방향으로 확산
def moveLeft(x):
    for i in range(1,c):
        room[x][i-1]=room[x][i]

# 아래쪽 방향으로 확산
def moveDown(start,end,y):
    for i in range(start,end,-1):
        room[i][y]=room[i-1][y]

# 오른쪽 방향으로 확산
def moveRight(x):
    for i in range(c-1,1,-1):
        room[x][i]=room[x][i-1]
    room[x][1]=0

# 위쪽 방향으로 확산
def moveUp(start,end,y):
    for i in range(start,end):
        room[i-1][y]=room[i][y]

r,c,t=map(int,sys.stdin.readline().split())
room=[list(map(int,sys.stdin.readline().split())) for _ in range(r)]
frash,dust=[],deque()
for i in range(r):
    if room[i][0]==-1:
        frash.append(i)
for _ in range(t):
    for i in range(r):
        for j in range(c):
            if room[i][j] > 4:
                dust.append([i, j])
    room=spread(room)
    airFrash()
reuslt=0
for r in room:
    reuslt+=sum(r)
print(reuslt+2)