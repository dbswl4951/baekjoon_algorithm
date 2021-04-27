#아기 상어
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 상어 이동, 먹을 수 있는 물고기 return
def moveShark(shark):
    x,y,size=shark
    q=deque()
    q.append([x,y])
    visited=[[-1]*n for _ in range(n)]
    visited[x][y]=0
    eatAble=[]     # 먹을 수 있는 모든 물고기 저장

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1 and size>=board[nx][ny]:
                visited[nx][ny]=visited[x][y]+1
                q.append([nx,ny])
                # 상어 크기보다 작은 물고기면 eatAble에 추가
                if 0<board[nx][ny]<size:
                    eatAble.append([visited[nx][ny],nx,ny])     # (상어로부터의 거리,x,y)
    if eatAble:
        eatAble.sort()
        return eatAble[0]
    return None

n=int(input().strip())
board=[]
shark=[]
for i in range(n):
    temp=list(map(int,input().split()))
    board.append(temp)
    for j in range(n):
        if temp[j]==9:
            shark.append(i)
            shark.append(j)
            shark.append(2)
            board[i][j]=0

result=0
exp=0   # 상어 경험치
while True:
    eatAble=moveShark(shark)
    if eatAble==None: break

    dist, fx, fy=eatAble
    board[fx][fy]=0
    exp+=1
    shark[0],shark[1]=fx,fy

    # 상어 크기만큼 물고기 먹으면 크기 up
    if exp==shark[2]:
        shark[2]+=1
        exp=0

    # 거리1당 1초
    result+=dist
print(result)