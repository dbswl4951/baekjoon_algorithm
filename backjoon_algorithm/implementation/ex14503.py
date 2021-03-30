#로봇 청소기
import sys

n,m = map(int,input().split())  #n:세로, m:가로
#현재위치:(x,y) , direction:방향 (0:북,1:동,2:남,3:서)
x,y,direction = map(int,input().split())
#북,동,남,서로 움질일 때의 좌표
dx=[-1,0,1,0]
dy=[0,1,0,-1]

room=[]     #장소의 벽, 빈 칸
for i in range(n):      #벽,빈 칸을 입력 받음
    room.append(list(map(int,sys.stdin.readline().split())))
cleaning=[[0]*m for _ in range(n)]   #로봇 청소기가 청소한 구역
cleaning[x][y]=1    #맨 처음 로봇 청소기의 좌표
turnTime=0  #회전한 횟수
count=1 #청소한 칸의 개수

while True: #시뮬레이션 시작
    #왼쪽으로 회전
    if direction==0:
        direction=3
    else:
        direction-=1
    ix=x+dx[direction]  #회전하고 이동했을 때의 x좌표
    iy=y+dy[direction]  #회전하고 이동했을 때의 y좌표

    if room[ix][iy]==0 and cleaning[ix][iy]==0: #벽이 아니고 청소되지 않았다면
        cleaning[ix][iy]=1  #청소함
        x,y=ix,iy   #전진
        turnTime=0
        count+=1
        continue
    else:
        turnTime+=1 #벽이거나 청소된 공간이면 회전

    if turnTime==4: #네 방향 모두 갈 수 없는 경우
        ix=x-dx[direction]  #후진했을 때 예상 위치
        iy=y-dy[direction]
        if room[ix][iy]==0:   #후진 할 수 있는 경우
            x=ix    #후진
            y=iy
        else:
            break
        turnTime = 0
print(count)