#소가 길을 건너간 이유6
'''
< 1차 시도 때 시간초과 원인? >
- road를 1차원 배열로 선언했기 때문에,
    not in 또는 in 썼을 때 모든 범위를 돌면서 탐색 해야 했기 때문!
- road를 3차원 배열로 선언하면
    (x,y)->(nx,ny)로 이동 할 경우,
    해당 좌표의 길 (road[x][y])만 탐색해주면 되므로 훨씬 탐색 범위가 적어진다!
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(cow):
    q=deque()
    q.append(cow)
    visited=[[0]*(n+1) for _ in range(n+1)]
    visited[cow[0]][cow[1]]=1
    meetCnt=0   # 소를 만난 횟수

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<nx<=n and 0<ny<=n and not visited[nx][ny] and (nx,ny) not in road[x][y]:
                visited[nx][ny]=1
                q.append([nx,ny])
                if board[nx][ny]==1:
                    meetCnt+=1
    # k마리 소 - 자기 자신(1) - 만난 횟수 =  길을 건너지 않으면 만날 수 없는 소들의 수
    return k-1-meetCnt

n,k,r=map(int,sys.stdin.readline().split())
road=[[[] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(r):
    a,b,c,d=map(int,input().split())
    road[a][b].append((c,d))
    road[c][d].append((a,b))
cows=list()
board=[[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a,b=map(int,input().split())
    cows.append((a,b))
    board[a][b]=1

result=0
for cow in cows:
    result+=bfs(cow)
print(result//2)


# 1차 시도 => 시간 초과
'''
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(c):
    global result
    q=deque()
    q.append(c)
    visited=[[0]*n for _ in range(n)]
    visited[c[0]][c[1]]=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                if [x,y,nx,ny] not in road:
                    if [nx,ny] in cow:
                        meetCow.append((nx,ny))
                    q.append([nx,ny])
                    visited[nx][ny]=1

n,k,r=map(int,sys.stdin.readline().split())
road=[]
for _ in range(r):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    road.append([x1-1,y1-1,x2-1,y2-1])
    road.append([x2-1,y2-1,x1-1,y1-1])
cow=[]
for _ in range(k):
    x,y=map(int,sys.stdin.readline().split())
    cow.append([x-1,y-1])

result=0
meetCow = []
for c in cow:
    bfs(c)
result+=len(meetCow)
print((k*(k-1)-result)//2)
'''