#아기 상어
'''
bfs를 돌면서
1) 현재 상어의 위치에서 먹을 수 있는 물고리를 모두 탐색 => 저장
2) 저장 된 물고기 (가장 가까운 물고기, 위쪽, 왼쪽)로 정렬 후, 맨 첫 번째 물고기만 먹고
3) 상어 이동 + 경험치 증가 (size 증가) + 시간 증가
하는 것이 포인트!!
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def start(sharkX,sharkY):
    q=deque()
    q.append([sharkX,sharkY])
    visited=[[0]*n for _ in range(n)]
    visited[sharkX][sharkY] = 1
    distance=[[0]*n for _ in range(n)]  # 상어로부터의 거리 저장
    ableEat=[]  #현재 위치에서 먹을 수 있는 물고기 저장 (x,y,상어로부터의 거리)
    while q:
        x,y=q.popleft()
        # 상하좌우 탐색하면서 먹을 수 있는 물고기 저장
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                # 상어보다 작거나 같은 물고기가 있는 경우 or 빈 공간 인 경우 => 방문
                if space[nx][ny]<=space[sharkX][sharkY] or space[nx][ny]==0:
                    visited[nx][ny] = 1
                    distance[nx][ny]=distance[x][y]+1
                    q.append([nx,ny])
                # 상어보다 작은 물고기 일 경우, 먹을 수 있는 물고기 list에 저장
                if space[nx][ny]<space[sharkX][sharkY] and space[nx][ny]!=0:
                    ableEat.append([nx,ny,distance[nx][ny]])

    # 먹을 수 있는 물고기가 없을 경우
    if not ableEat: return -1,-1,-1
    ableEat.sort(key=lambda x:(x[2],x[0],x[1]))
    # 먹을 수 있는 물고기 중, 가장 가까운 왼쪽 위 물고기 return
    return ableEat[0]

n=int(sys.stdin.readline().strip())
space=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
sharkX,sharkY=0,0
for i in range(n):
    for j in range(n):
        if space[i][j]==9:
            sharkX,sharkY=i,j
            # 상어의 위치를 상어의 크기로 저장
            space[i][j]=2

exp=0   # 상어 크기 경험치
time=0  # 소요 시간
while True:
    fishX,fishY,dist=start(sharkX,sharkY)
    if dist==-1 : break
    space[fishX][fishY]=space[sharkX][sharkY]
    space[sharkX][sharkY]=0
    sharkX,sharkY=fishX,fishY
    exp+=1
    # 움직인 거리만큼 +시간
    time+=dist
    # 상어 크기만큼 물고기를 먹었다면, 크기+1
    if exp==space[sharkX][sharkY]:
        space[sharkX][sharkY]+=1
        exp=0

print(time)