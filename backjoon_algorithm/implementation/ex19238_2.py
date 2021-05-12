#스타트 택시
'''
- 손님을 목적지에 내려주면 연료 충전
- 택시, 승객 같은 위치에 있을 시, 거리 0
- 1칸 이동 시, 연료 1씩 소비

1. 현재 위치에서 가장 가까운 승객 선택
    1) 위치 같은 승객 여러명 => 행 작은 승객 선택
    2) 행 같은 승객 여려명 => 열이 작은 승객 선택
2. 승객 목적지로 이동 (이동 칸 수만큼 연료 -)
    1) 이동 중에 연료 바닥? 이동 실패, 업무 끝
3. 목적지에 도달하면 손님 태운 뒤 소모한 연료X2 충전 됨

모든 손님을 이동 시킬 수 없는 경우, 목적지 도달 불가능 한 경우 => -1 출력
있는 경우 => 남은 연료 출력
'''
from collections import deque

dx=[0,-1,1,0,0]
dy=[0,0,0,-1,1]

# 가장 가까운 승객 선택
def selectPassenger():
    global tx,ty
    q=deque()
    q.append([tx,ty])
    visited=[[-1]*n for _ in range(n)]
    passengersInfo=[]   # (거리,x,y,승객 번호)

    while q:
        x,y=q.popleft()
        for i in range(5):
            nx,ny=x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny]==-1 and board[nx][ny]!=1:
                visited[nx][ny]=visited[x][y]+1
                q.append([nx,ny])
                # 승객 만남
                if passengers[nx][ny]:
                    for pNum in passengers[nx][ny]:
                        if pNum>0:
                            passengersInfo.append([visited[nx][ny],nx,ny,pNum])

    if passengersInfo:
        passengersInfo.sort()
        p=passengersInfo[0]
        passengers[p[1]][p[2]].remove(p[3])
        return p
    else: return None

# 승객 태운 뒤, 목적지로 이동
def moveTodestination(num):
    q=deque()
    q.append([tx,ty])
    visited=[[-1]*n for _ in range(n)]

    while q:
        x, y = q.popleft()
        for i in range(5):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1 and board[nx][ny]!=1:
                visited[nx][ny]=visited[x][y]+1
                # 도착지 도달
                if num in passengers[nx][ny]:
                    passengers[nx][ny].remove(num)
                    return visited[nx][ny],nx,ny
                q.append([nx,ny])
    # 도착지에 도달 불가능 한 경우
    return None,None,None

n,m,fuel=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
tx,ty=map(int,input().split())      # 택시 (x,y) 좌표
tx,ty=tx-1,ty-1
passengers=[[[] for _ in range(n)] for _ in range(n)]       # 승객의 (시작x, 시작y, 도착x, 도착y) 좌표
for i in range(1,m+1):
    a,b,c,d=map(int,input().split())
    passengers[a-1][b-1].append(i)       # passengers에 승객 시작 지점 1번부터 표시
    passengers[c-1][d-1].append(-i)       # passengers에 승객 도착 지점 -1부터 표시

flag=0
suceess=0   # 목적지까지 도달 한 승객 수
for i in range(m):
    # 가장 가까운 승객 선택
    passenger=selectPassenger()
    # 손님까지 도달 할 수 없는 경우
    if passenger==None:
        flag=1; break
    # 이동한 거리만큼 연로-
    fuel-=passenger[0]
    if fuel<0:
        flag=1; break
    tx,ty=passenger[1],passenger[2]

    # 승객 태운 뒤, 목적지로 이동
    f,ex,ey=moveTodestination(-passenger[3])
    # 도착지에 도달 불가능 한 경우
    if f==None:
        flag=1; break
    tx,ty=ex,ey
    fuel-=f
    if fuel < 0:
        flag = 1; break
    fuel+=(2*f)
    suceess+=1

if flag: print(-1)
else: print(fuel)