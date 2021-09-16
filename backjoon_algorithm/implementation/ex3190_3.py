#뱀
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def changeDir(dir,d):
    if dir=='D':
        if d==0: return 3
        elif d==1: return 2
        elif d==2: return 0
        else: return 1
    else:
        if d==0: return 2
        elif d==1: return 3
        elif d==2: return 1
        else: return 0

n= int(sys.stdin.readline().strip())
k= int(sys.stdin.readline().strip())
apple=[list(map(int,sys.stdin.readline().split())) for _ in range(k)]
l = int(sys.stdin.readline().strip())
moveTime, moveDir=[],[]
for _ in range(l):
    a,b = sys.stdin.readline().split()
    moveTime.append(int(a))
    moveDir.append(b)
time,d,moveIdx=0,3,0
sneak = deque()
sneak.append([1,1])

while True:
    x,y = sneak[0]
    # 1. d방향으로 이동
    nx,ny = x+dx[d],y+dy[d]
    time+=1

    # 2. 몸통과 만나는지, 범위 밖인지 check
    if not(1<=nx<=n and 1<=ny<=n) or [nx,ny] in sneak: break

    sneak.appendleft([nx,ny])
    # 3. 사과 있으면 먹고 사과 삭제. 사과 없으면 꼬리 줄어듦
    if not [nx,ny] in apple:
        sneak.pop()
    else:
        apple.remove([nx,ny])

    # 4. 방향 변경
    if moveIdx<len(moveTime) and time == moveTime[moveIdx]:
        d = changeDir(moveDir[moveIdx],d)
        moveIdx += 1
print(time)