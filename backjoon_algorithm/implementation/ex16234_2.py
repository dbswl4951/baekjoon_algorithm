#인구 이동
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 연합 찾기
def findUnit(x,y):
    pSum,nSum=board[x][y],1   # 인구 총 합, 나라 개수
    q=deque()
    q.append([x,y])
    nq=deque()  # 연합국 모두 저장
    nq.append([x,y])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and l<=abs(board[x][y]-board[nx][ny])<=r:
                visited[nx][ny]=1
                q.append([nx,ny])
                pSum+=board[nx][ny]
                nSum+=1
                nq.append([nx,ny])

    # 인구수 새로 갱신
    po=pSum//nSum
    if nSum>1:
        for nx,ny in nq:
            board[nx][ny]=po

    if nSum>1: return True
    return False

n,l,r=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
result=0
while True:
    flag=0
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j]=1
                if findUnit(i,j): flag=1
    if not flag: break
    result += 1
print(result)

