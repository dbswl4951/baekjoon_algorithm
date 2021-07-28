#말이 되고픈 원숭이
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]
hdx=[1,2,1,2,-2,-1,-2,-1]
hdy=[2,1,-2,-1,-1,-2,1,2]

def bfs():
    q=deque()
    q.append([0,0,k,0])
    # visited[x][y][r] : 말 이동 횟수가 r번 남은 (x,y)에서의 총 이동횟수
    visited=[[[0]*(k+1) for _ in range(w)] for _ in range(h)]

    while q:
        x,y,r,cnt=q.popleft()
        if x==h-1 and y==w-1: return cnt

        # 말의 이동방식으로 갈 수 있는 경우
        if r>0:
            for i in range(8):
                nx,ny=x+hdx[i],y+hdy[i]
                if 0<=nx<h and 0<=ny<w and not visited[nx][ny][r-1] and not board[nx][ny]:
                    visited[nx][ny][r-1]=1
                    q.append([nx,ny,r-1,cnt+1])

        # 인접한 칸으로 이동 하는 경우
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny][r] and not board[nx][ny]:
                visited[nx][ny][r]=1
                q.append([nx, ny, r,cnt+1])
    return -1

k=int(sys.stdin.readline().strip())
w,h=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(h)]
print(bfs())