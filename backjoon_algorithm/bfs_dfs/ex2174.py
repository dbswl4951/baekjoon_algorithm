#로봇 시뮬레이션
from collections import deque
import sys

direction={'N':[-1,0],'S':[1,0],'W':[0,-1],'E':[0,1]}

#로봇이 향하고 있는 방향을 기준으로 앞으로 한 칸 움직임
def functionF(x,y,d):
    d=direction[d]
    return x+d[0],y+d[1]

#로봇이 향하고 있는 방향을 기준으로 왼쪽으로 90도 회전
def functionL(d):
    if d=='N': return 'W'
    elif d=='W': return 'S'
    elif d=='S': return 'E'
    else: return 'N'

#로봇이 향하고 있는 방향을 기준으로 오른쪽으로 90도 회전
def functionR(d):
    if d=='N': return 'E'
    elif d=='E': return 'S'
    elif d=='S': return 'W'
    else: return 'N'

def bfs(robotNum,order,repeat):
    for i in range(repeat):
        x, y, d = robot[robotNum]
        x, y = int(x), int(y)
        #왼쪽 90도 회전
        if order=='L':
            robot[robotNum]=[x,y,functionL(d)]
        #오른쪽 90도 회전
        elif order=='R':
            robot[robotNum]=[x,y,functionR(d)]
        #앞으로 한 칸 이동
        else:
            nx,ny=functionF(x,y,d)
            if 1<=nx<=b and 1<=ny<=a:
                robot[robotNum]=[nx,ny,d]
                x,y=nx,ny
            #로봇이 벽에 충돌 하는 경우
            else:
                print("Robot "+str(robotNum)+" crashes into the wall")
                sys.exit(0)
        for key,value in robot.items():
            if key==robotNum: continue
            if x==value[0] and y==value[1]:
                print("Robot "+str(robotNum)+" crashes into robot "+str(key))
                sys.exit(0)
    position.append([x,y])

a,b=map(int,sys.stdin.readline().split())   #가로,세로
n,m =map(int,sys.stdin.readline().split())  #로봇 수, 명령 수
robot,orders,position= {},deque(),deque()
for i in range(n):
    y,x,d = sys.stdin.readline().split()
    robot[i+1]=[b-int(x)+1,int(y),d]   #(x좌표, y좌표, 현재 방향)
    position.append([b-int(x)+1,int(y)])
for _ in range(m):
    robotNum,orderNum,repeat=sys.stdin.readline().split()
    orders.append([int(robotNum),orderNum,int(repeat)])
while orders:
    robotNum, order, repeat=orders.popleft()
    position.popleft()
    bfs(robotNum,order,repeat)
print("OK")