#미친 아두이노
import sys
from collections import deque

dx=[1,1,1,0,0,0,-1,-1,-1]
dy=[-1,0,1,-1,0,1,-1,0,1]

# 아두이노의 이동 방향 구하기
def getDir(mx,my,ax,ay):
    dist=int(1e9)
    dir=10
    for i in range(9):
        temp=abs(mx - (ax+dx[i])) + abs(my - (ay+dy[i]))
        if temp<dist:
            dist=temp
            dir=i
    return dir

def bfs(mx,my,d):
    arduinoDic=dict()   # 이동 후, 아두이노의 방향 저장

    nmx,nmy=mx+dx[d],my+dy[d]
    # 종수가 이동 한 칸에 아두이노가 있는 경우 => 실패
    if board[nmx][nmy]=='R': return -1,-1
    board[mx][my] = '.'
    board[nmx][nmy]='I'

    while arduinos:
        ax,ay=arduinos.popleft()

        dir=getDir(nmx,nmy,ax,ay)
        # 아두이노가 종수의 위치쪽으로 이동
        nax,nay=ax+dx[dir],ay+dy[dir]
        board[ax][ay]='.'

        # 아두이노가 종수랑 만났을 때 => 실패
        if board[nax][nay]=='I': return -1,-1
        if (nax,nay) in arduinoDic:
            arduinoDic[(nax,nay)]+=1
        else:
            arduinoDic[(nax,nay)]=1

    # 아두이노 이동 or 폭발
    for key,value in arduinoDic.items():
        # 아두이노끼리 만나면 폭발
        if value>1: continue
        # 아두이노가 종수 만나면 => 실패
        if board[key[0]][key[1]]=='I': return -1,-1
        arduinos.append(key)
        board[key[0]][key[1]]='R'
    return nmx,nmy

r,c=map(int,sys.stdin.readline().split())
board=[list(sys.stdin.readline().strip()) for _ in range(r)]
move=list(map(int,sys.stdin.readline().strip()))
mx,my=0,0   # 종수 위치
arduinos=deque()    # 아두이노 위치
for i in range(r):
    for j in range(c):
        if board[i][j]=='I': mx,my=i,j
        elif board[i][j]=='R': arduinos.append((i,j))

result=0
for m in move:
    result += 1
    mx,my=bfs(mx,my,m-1)
    if mx==-1:
        print('kraj', result)
        sys.exit(0)
for i in range(r):
    for j in range(c):
        print(board[i][j],end='')
    print()