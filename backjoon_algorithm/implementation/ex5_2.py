#게임 개발2
import sys

n,m = map(int,input().split())     #n:세로, m:가로
a,b,direction = map(int,input().split())    #현재위치:(a,b) , d:방향 (0:북,1:동,2:남,3:서)
count=1     #방문한 칸의 수
d=[[0]*m for _ in range(n)]     #방문한 위치 저장
d[a][b]=1   #현재 위치 방문 처리

gameMap=[]      #전체 맵
for i in range(n):
    gameMap.append(list(map(int,sys.stdin.readline().split())))

#븍,동,남,서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():    #왼쪽으로 90도 회전
    global direction
    direction-=1
    if direction==-1:
        direction=3

turn_time=0
while True:
    print("direction::",direction)
    print("a:::",a," b:::",b)
    print("turn:::",turn_time)

    turn_left()
    nx=a+dx[direction]  #이동후 예상 x좌표
    ny=b+dy[direction]  #이동후 예상 y좌표
    if d[nx][ny]==0 and gameMap[nx][ny]==0:     #방문하지 않은 칸이 있는경우
        d[nx][ny]=1
        a=nx
        b=ny
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1

    if turn_time==4:    #네 방향 모두 갈 수 없는 경우
        nx=a-dx[direction]      #예상 좌표 원래대로
        ny=b-dy[direction]
        if gameMap[nx][ny]==0:  #뒤로 갈 수 있으면 뒤로 가기
            a=nx
            b=ny
        else:   #뒤로 갈 수 없으면 종료
            break
        turn_time=0

print(count)