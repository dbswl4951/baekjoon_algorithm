#탈출
'''
bfs를 물, 고슴도치 둘 다에 적용 시키는 문제
고슴도치는 물이 찰 예정인 칸으로 이동 불가므로, 물부터 이동 시켜야 함

1. 한 함수에서 같은 while q: 문으로 물이랑 고슴도치 이동 둘 다 하려고 한게 miss!!!
=> spreadWater(), bfs() 두 개로 나눠 다른 while문으로 돌려줘야 함
2. bfs 함수 안에 while문 2개가 왜 필요 한지 몰라서 헤맸음
=> 큰 while문은 고슴도치가 도착지까지 도달하기 위한 반복문.
=> 작은 while문은 고슴도치가 있을 수 있는 한 지점에서 여러 방향으로 움직일 때 사용
 ex) 고슴도치가 f[2][2],f[2][4]에 있을 수 있다면 f[2][2]에서 상하좌우, f[2][4]에서 상하좌우 2번씩 탐색 해야 하므로
 작은 while문은 2번 반복하는 역할
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def spreadWater(): # 물 채우기
    global water
    wl=len(water)
    while wl>0:
        x, y = water.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if forest[nx][ny] == '.':
                    forest[nx][ny] = '*'
                    water.append([nx, ny])
        wl -= 1

def bfs(startX,startY):
    visited = [[0] * c for _ in range(r)]
    visited[startX][startY]=1
    q=deque()
    q.append([startX,startY])
    while q:    #전체 맵에서 고슴도치가 완전히 굴에 도착 할 때 까지 반복
        ql=len(q)
        while ql>0: #고슴도치가 한 위치에서 여러 방향으로 갈 때, 갈 수 있는 곳인지 체크 하는 반복문
            x,y=q.popleft()
            for i in range(4):  #고슴도치 이동
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<r and 0<=ny<c and visited[nx][ny]==0:
                    if forest[nx][ny] == '.':
                        visited[nx][ny]=visited[x][y]+1
                        q.append([nx,ny])
                        forest[x][y]='.'
                        forest[nx][ny]='S'
                    elif forest[nx][ny] == 'D': #도착지점 도달
                        print(visited[x][y])
                        return
            ql-=1
        spreadWater()
    print("KAKTUS")
    return

r,c=map(int,sys.stdin.readline().split())
forest=[]
for _ in range(r):
    forest.append(list(sys.stdin.readline().strip()))
water=deque()
for i in range(r):  #고슴도치, 물 위치 찾기
    for j in range(c):
        if forest[i][j]=='S':
            startX,startY=i,j
        elif forest[i][j]=='*':
            water.append([i,j])
spreadWater()
bfs(startX,startY)