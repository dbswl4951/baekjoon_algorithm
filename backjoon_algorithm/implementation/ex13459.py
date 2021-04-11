#구슬 탈출
'''
4차원 배열 사용 할 생각을 못했다.
어렵다 ^.ㅜ
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 구슬 이동
def move(x,y,d):
    cnt=0   # 움직인 칸 수
    while board[x+dx[d]][y+dy[d]]!='#' and board[x][y]!='O':
        x,y=x+dx[d],y+dy[d]
        cnt+=1
    return x,y,cnt

def gameStart():
    while q:
        rx,ry,bx,by,cnt=q.popleft()
        if cnt>10: break
        for i in range(4):
            # nrx,nry,rc = (이동 후 x, 이동 후 y, 움직인 칸)
            nrx,nry,rc=move(rx,ry,i)
            nbx,nby,bc=move(bx,by,i)
            if board[nbx][nby]!='O':
                # 파란 구슬이 구멍에 도착하지 않고, 빨간 구슬만 도착
                if board[nrx][nry]=='O':
                    print(1)
                    return
                if nrx==nbx and nry==nby:
                    # 빨간 구슬이 더 많이 이동 => 빨간 구슬이 한 칸 뒤로
                    if rc>bc:
                        nrx,nry=nrx-dx[i],nry-dy[i]
                    # 파란 구슬이 더 많이 이동 => 파란 구슬이 한 칸 뒤로
                    else:
                        nbx, nby = nbx - dx[i], nby - dy[i]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby]=1
                    q.append([nrx,nry,nbx,nby,cnt+1])
    print(0)

n,m=map(int,sys.stdin.readline().split())
board=[list(sys.stdin.readline().strip()) for _ in range(n)]
rx,ry,bx,by=0,0,0,0,
for i in range(n):
    for j in range(m):
        if board[i][j]=='R':
            rx,ry=i,j
        elif board[i][j]=='B':
            bx,by=i,j
q=deque()
q.append([rx,ry,bx,by,1])
visited=[[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
visited[rx][ry][bx][by]=1
gameStart()