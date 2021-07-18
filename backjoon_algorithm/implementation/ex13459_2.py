#구슬 탈출
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    q=deque()
    q.append([srx,sry,sbx,sby,-1,0])    # (빨간 구슬x, 빨간 구슬y, 파란 구슬x, 파란 구슬y, 그 전 방향, 이동횟수)

    while q:
        rx,ry,bx,by,dir,cnt=q.popleft()
        # 이동 횟수가 10회 이상이면 종료 => 실패
        if cnt>=10: break

        for i in range(4):
            rFlag, bFlag = 0, 0     # rFlag: 빨간 구슬이 도착했는지, bFlag: 파란 구슬이 도착했는지
            # 그 전 방향으로 돌아가는거 막음
            if (dir== 0and i == 1) or (dir==1 and i == 0) or (dir==2 and i==3) or (dir== 3and i==2): continue
            rBlock, bBlock = 0, 0       # 다른 구슬에게 막힘 표시
            nrx,nry,nbx,nby=rx,ry,bx,by

            # 빨간 구슬 옮기기
            while 0<nrx<n-1 and 0<nry<m-1:
                nrx, nry=nrx+dx[i],nry+dy[i]
                if board[nrx][nry]=='#':
                    nrx, nry = nrx - dx[i], nry-dy[i]
                    break
                if board[nrx][nry]=='O':
                    rFlag=1
                    break
                # 파란 구슬 만남
                if nrx==bx and nry==by: rBlock=1

            # 파란 구슬 옮기기
            while 0<nbx<n-1 and 0<nby<m-1:
                nbx, nby = nbx + dx[i], nby + dy[i]
                if board[nbx][nby] == '#':
                    nbx, nby = nbx-dx[i], nby-dy[i]
                    break
                if board[nbx][nby] == 'O':
                    bFlag=1
                    break
                # 빨간 구슬 만남
                if nbx==rx and nby==ry: bBlock = 1

            # 파란 구슬이 구멍에 들어가면 다음 turn으로
            if bFlag: continue
            # 빨간 구슬만 들어가면 바로 성공
            if rFlag and not bFlag:
                print(1)
                sys.exit(0)

            if rx == nrx and ry == nry and bx == nbx and by == nby: continue
            # 다른 구슬한테 진로 막히면, 막은 구슬의 한 칸 전으로 이동
            if rBlock:
                nrx, nry = nbx - dx[i], nby - dy[i]
            if bBlock:
                nbx, nby = nrx - dx[i], nry - dy[i]
            q.append([nrx,nry,nbx,nby,i,cnt+1])
    print(0)

n,m=map(int,sys.stdin.readline().split())
board=[list(sys.stdin.readline().strip()) for _ in range(n)]
srx,sry,sbx,sby=0,0,0,0
for i in range(n):
    for j in range(m):
        if board[i][j]=='R':
            srx=i; sry=j
        elif board[i][j]=='B':
            sbx=i; sby=j
bfs()