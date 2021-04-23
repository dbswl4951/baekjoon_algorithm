#두 동전
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(cnt):
    global result,coin
    # 실패
    if cnt>10 or cnt>=result: return

    for i in range(4):
        before=[]     # 동전 이동 전 좌표 저장
        drop=0
        for j in range(2):
            c=coin[j]
            before.append(c)
            nx,ny=c[0]+dx[i],c[1]+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]=='.':
                    coin[j]=[nx,ny]
            else:
                coin[j]=[nx,ny]
                drop+=1

        # 이동 후 좌표가 그 전 좌표와 같거나 동전 2개 다 떨어지면, 다음 방향 탐색
        if before==coin or drop==2:
            coin=before
            continue
        elif drop==1:
            result=min(cnt,result)
            return
        else:
            dfs(cnt+1)
        # 이동 전으로 돌아가기
        coin=before

n,m=map(int,sys.stdin.readline().split())
board=[list(sys.stdin.readline().strip()) for _ in range(n)]
coin=deque()
for i in range(n):
    for j in range(m):
        if board[i][j]=='o':
            coin.append([i,j])
result=11
dfs(1)
if result==11: print(-1)
else: print(result)