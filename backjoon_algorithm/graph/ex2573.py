#빙산
'''
bfs 2번 사용 + pypy3 통과 (python3 시간초과)
1. 1년단위로 빙산이 줄어드는 함수 melting
 => 상하좌우 확인 후 0칸의 수대로 빙산의 높이-
2. 빙산이 분리 됐는지 확인하는 함수 separate
 => 경로 탐색

처음에 무조건 한덩어리 빙산만 주어짐을 못보고 삽질함..
앞으로 문제를 잘 읽어보자ㅜㅜ
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def melting():  #빙산 녹이기
    global mq
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0:
                mq.append([i, j])
    while mq:
        x,y=mq.popleft()
        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and ice[nx][ny]==0 and ice[x][y]>0:
                #같은 턴에서 없어진 빙산은 다음 빙산 녹이기에 영향을 주면 안된다. 따라서 녹아서 없어진 빙산은 -1로 설정 후, 턴이 끝나면 0으로 바꿔 줌
                ice[x][y]-=1
                if ice[x][y]==0:    ice[x][y]=-1
    for i in range(n):
        for j in range(m):
            if ice[i][j] ==-1:
                ice[i][j]=0
    return ice

def separate(x,y): #분리된 빙산 구하기
    global sq
    visited[x][y] = 1
    sq.append([x,y])
    while sq:
        x, y = sq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m and ice[nx][ny]!=0 and visited[nx][ny]==0:
                visited[nx][ny]=1
                sq.append([nx,ny])

n,m=map(int,sys.stdin.readline().split())
ice=[]
for i in range(n):
    ice.append(list(map(int,sys.stdin.readline().split())))
mq,sq = deque(),deque()
result=0
while True:
    iceTemp=melting()
    temp=0
    for i in iceTemp:
        temp+=i.count(0)
    if temp==n*m:   #만약 분리되지 않고 빙산이 다 녹았다면 0 출력 후, 프로그램 종료
        print(0)
        sys.exit(0)
    visited = [[0] * m for _ in range(n)]
    count = 0
    result+=1
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0 and visited[i][j]==0:
                separate(i,j)
                count+=1
                if count>1: #분리된 빙산이 2개 이상이면 년도 수(result) 출력
                    print(result)
                    sys.exit(0)