#아기 상어
'''
bfs알고리즘 사용 (가장 가까운 물고기를 먼저 먹는다)
bfs로 자기가 먹을 수 있는 물고기를 찾는다.
'''
from collections import deque   #양방향에서 데이터를 처리할 수 있는 queue형 자료구조

def start(sharkX,sharkY):
    eat=[]  #먹을 수 있는 물고기 x,y좌표,상어와의 거리
    dist=[[0]*n for i in range(n)]      #상어가 있는 곳으로부터의 거리
    visited=[[0]*n for i in range(n)]     #상어가 지나간 곳
    visited[sharkX][sharkY]=1
    q=deque()   #앞으로 들려야 할 좌표를 저장
    q.append([sharkX,sharkY])

    while q:  # 들려야 할 좌표가 존재한다면
        x, y = q.popleft()  # 기준이 되는 좌표 pop
        for i in range(4):  # 방향 4번 다 실행
            nextX = x + directionX[i]
            nextY = y + directionY[i]
            if 0 <= nextX < n and 0 <= nextY < n and visited[nextX][nextY] == 0:  # 방문하지 않았다면
                # 빈 칸이거나 상어보다 작거나 큰 물고기가 있으면 방문
                if space[nextX][nextY] <= space[sharkX][sharkY] or space[nextX][nextY] == 0:
                    q.append([nextX, nextY])  # 큐에 현재 좌표를 넣음 (다음번 pop할 때 방문)
                    visited[nextX][nextY] = 1
                    dist[nextX][nextY] = dist[x][y] + 1  # 현재위치로부터 거리 저장
                # 상어보다 작은 물고기가 있으면
                if space[nextX][nextY] < space[sharkX][sharkY] and space[nextX][nextY] != 0:
                    eat.append([nextX, nextY, dist[nextX][nextY]])  # 물고기의 좌표와 상어로부터의 거리 저장
    if not eat: #먹을 수 있는 물고기가 없으면 -1 리턴
        return -1,-1,-1
    eat.sort(key=lambda x: (x[2], x[0], x[1]))     #거리,x,y좌표를 기준으로 물고기 정렬 (가장 위, 가장 왼쪽)
    return eat[0][0],eat[0][1],eat[0][2]    #먹을 수 있는 물고기 중 가장 가까운 첫번째 물고기 return

#아래,위,왼쪽,오른쪽 방향 이동
directionX=[1, -1, 0, 0]
directionY=[0, 0, -1, 1]
sharkX,sharkY=0,0   #상어 위치
n=int(input())
space=[]    #전체 맵
for i in range(n):
    space.append(list(map(int,input().split())))
for i in range(len(space)):
    for j in range(len(space[0])):
        if space[i][j]==9:  #초기 상어의 위치 저장
            sharkX,sharkY=i,j
            space[i][j]=2   #상어의 위치를 상어의 크기로 설정

exp=0   #경험치
count=0     #소요 시간
while True:
    fishX,fishY,dist=start(sharkX,sharkY)
    if fishX==-1: break    #먹을 수 있는 물고기 없으면 break
    space[fishX][fishY]=space[sharkX][sharkY]    #물고기 위치로 상어 이동
    space[sharkX][sharkY]=0 #원래 상어가 있던 곳은 0으로 설정
    sharkX,sharkY=fishX,fishY
    exp+=1  #물고기 한마리 먹어서 경험치+=1
    if exp==space[sharkX][sharkY]:  #경험치와 상어의 크기가 같다면
        space[fishX][fishY]+=1    #상어크기+=1
        exp=0
    count+=dist #1초에 거리1씩 움직이므로, 움직인 거리만큼 count에 더해줌
print(count)