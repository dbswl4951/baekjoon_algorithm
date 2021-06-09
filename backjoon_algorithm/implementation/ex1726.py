#로봇
'''
visited를 3차원 배열로 설정하는게 생각하기 어려웠다
visitied[x][y]=[0,0,0,0]으로 각각 (x,y)에서의 동,서,남,북의 방향을 가지고 들렸는지 방문 체크 하는 용도로 사용
또한 위치, 방향 중 하나라도 변경이 되면 큐에 삽입 해야 함
'''
import sys
from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs():
    q=deque()
    q.append([sx,sy,sd,0])
    visited[sx][sy][sd]=1

    while q:
        x,y,d,cnt=q.popleft()
        if x==ex and y==ey and d==ed: return cnt

        # 현재 방향으로 이동 (최대 3칸)+
        
        nx,ny=x,y
        for i in range(3):
            nx,ny=nx+dx[d],ny+dy[d]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]==0:
                if not visited[nx][ny][d]:
                    visited[nx][ny][d]=1
                    q.append([nx,ny,d,cnt+1])
            else: break

        # 방향 바꾸기
        for i in range(4):
            if i!=d and not visited[x][y][i]:
                visited[x][y][i]=1
                # 두 번 회전 한 경우
                if (d==0 and i==1) or (d==1 and i==0) or (d==2 and i==3) or (d==3 and i==2):
                    q.append([x,y,i,cnt+2])
                else:
                    q.append([x,y,i,cnt+1])

n,m=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
sx,sy,sd=map(int,sys.stdin.readline().split())
ex,ey,ed=map(int,sys.stdin.readline().split())
sx-=1;sy-=1;sd-=1;ex-=1;ey-=1;ed-=1
visited=[[[0]*4 for _ in range(m)] for _ in range(n)]
print(bfs())