#벽 부수고 이동하기
'''
최단 경로 => BFS (너비우선탐색) 사용!
처음에는 벽을 부수지않고 이동 할 때와 벽을 부순 후 이동 할 때를 나누지 않고 코드 작성 해서 실패..
벽을 부수지 않고 이동할 때와 벽을 부순 후의 이동으로 차원을 나누어서 계산해야 함!!
'''
import sys
from collections import deque

#상하좌우 이동
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bsf():
    q = deque()
    q.append([0, 0, 1])
    # visitied[x][y][0]은 벽을 뚫은 이후, 시작지점으로부터의 거리
    # visitied[x][y][1]이 1이면 벽을 뚫을 수 있는 상태. 0아면 벽을 뚫은 상태. 2이상은 벽을 뚫기 전 시작지점으로부터의 거리
    visit = [[[0] * 2 for i in range(m)] for i in range(n)]
    visit[0][0][1] = 1
    while q:
        x,y,w = q.popleft()
        if x==n-1 and y==m-1:   #출구 도달
            return visit[x][y][w]
        for i in range(4):  #상하좌우 방향으로 탐색
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]==1 and w==1:   #움직인 곳이 벽이 있고, 벽을 부술수 있다면(w=1)
                    visit[nx][ny][0]=visit[x][y][1]+1
                    q.append([nx,ny,0]) #벽을 한 번 부순 후 w=0으로 설정 (다음부턴 벽을 부실 수 없음)
                elif board[nx][ny]==0 and visit[nx][ny][w]==0:    #빈 칸이고, 방문하지 않았다면
                    visit[nx][ny][w]=visit[x][y][w]+1   #그전까지의 거리 +1
                    q.append([nx,ny,w])
    return -1

n,m=map(int,sys.stdin.readline().split())
board=[]
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().strip())))
print(bsf())