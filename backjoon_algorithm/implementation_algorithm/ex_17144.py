#미세먼지 안녕!
'''
먼지 확산, 공기 청정기 작동이 한 큐에 한 번씩 번갈아 가며 t만큼 수행 되야 한다.

알고리즘 자체는 어렵지 않았는데, 범위 설정을 잘못해서 바로 잡느라 시간이 꽤 걸린 문제
'''
import sys,math
from collections import deque

#아래,왼쪽,위,오른쪽
dx=[1,0,-1,0]
dy=[0,-1,0,1]

#먼지 확산 시키기
def spread():
    for i in range(r):
        for j in range(c):
            if room[i][j]>4:
                dust.append([i, j])
    speadList=[]
    while dust:
        x,y=dust.popleft()
        d=math.trunc(room[x][y]/5)
        if d!=0:
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<r and 0<=ny<c and room[nx][ny]!=-1:
                    room[x][y] -= d
                    speadList.append([nx,ny,d])
    for sl in speadList:
        x,y,d=sl
        room[x][y]+=d

def moveRight(x):
        for i in range(c - 2, -1, -1):  # 왼쪽->오른쪽
            if room[x][i] != 0 and room[x][i] != -1:
                room[x][i + 1] = room[x][i]
                room[x][i] = 0

def moveLeft(y,d):
    if d==1:
        for i in range(y+1,c):  # 오른쪽->왼쪽
            if room[0][i] != 0:
                room[0][i - 1] = room[0][i]
                room[0][i] = 0
    else:
        for i in range(y+1,c):  # 오른쪽->왼쪽
            if room[r-1][i] != 0:
                room[r-1][i - 1] = room[r-1][i]
                room[r-1][i] = 0

#공기 청정기 작동
def clearAir(t):
    while t>0:
        spread()
        #공기 청정기 위쪽
        x,y=cleaner[0][0],cleaner[0][1]
        for i in range(x-1,-1,-1):  #위->아래
            if room[i][0]!=0:
                if room[i+1][0]==-1: room[i][0]=0   #공기청정기 만나면 먼지 삭제
                else:
                    room[i+1][0]= room[i][0]  #먼지 한 칸 이동
                    room[i][0]=0
        moveLeft(y,1)
        for i in range(1,x+1):   #아래->위
            if room[i][c-1] != 0:
                room[i-1][c-1]=room[i][c-1]
                room[i][c-1]=0
        moveRight(x)
        #공기 청정기 아래쪽
        x, y = cleaner[1][0], cleaner[1][1]
        for i in range(x+1,r):  #아래->위
            if room[i][0]!=0:
                if room[i-1][0]==-1: room[i][0]=0   #공기청정기 만나면 먼지 삭제
                else:
                    room[i-1][0]= room[i][0]  #먼지 한 칸 이동
                    room[i][0]=0
        moveLeft(y,2)
        for i in range(r-2,x-1,-1):   #위->아래
            if room[i][c-1] != 0:
                room[i+1][c-1]=room[i][c-1]
                room[i][c-1]=0
        moveRight(x)
        t-=1

r,c,t=map(int,sys.stdin.readline().split()) #가로, 세로, 초
room=[]
for _ in range(r):
    room.append(list(map(int,sys.stdin.readline().split())))
dust=deque()
cleaner=[]
#먼지, 공기 청정기 위치 dust 큐에 삽입
for i in range(r):
    for j in range(c):
        if room[i][j]==-1:
            cleaner.append([i,j])
clearAir(t)
result=0
for i in range(r):
    for j in range(c):
        if room[i][j]!=0 and room[i][j]!=-1:
            result+=room[i][j]
print(result)