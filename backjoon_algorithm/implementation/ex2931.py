#가스관
import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 파이프의 모양에 따라 갈 수 있는 모든 위치 반환
def getDir(p):
    if p=='|':
        return [1, 3]
    elif p == '-':
        return [0, 2]
    elif p == '+' or p == 'M' or p == 'Z':
        return [0, 1, 2, 3]
    elif p == '1':
        return [0, 1]
    elif p == '2':
        return [0, 3]
    elif p == '3':
        return [2, 3]
    elif p == '4':
        return [1, 2]

def bfs(x,y,dir):
    global px,py

    q=deque()
    q.append([x,y,dir])

    while q:
        x,y,dir = q.popleft()
        for d in dir:
            nx,ny = x+dx[d],y+dy[d]
            if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
                if board[nx][ny]!='.':
                    visited[nx][ny]=1
                    # 현재 파이프를 통해 갈 수 있는 모든 방향 구함
                    nDir = getDir(board[nx][ny])
                    q.append([nx,ny,nDir])
                else:
                    # M, Z에 이어진 파이프는 무조건 한 개
                    if board[x][y]=='M' or board[x][y]=='Z': continue
                    if not px and not py: px,py = nx+1,ny+1
                    # 온 방향과 반대 방향 구하기
                    nd = (d+2)%4
                    if nd not in pipeList: pipeList.append(nd)

r,c = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(r)]
mx,my,zx,zy = 0,0,0,0
pipeList,px,py=[],0,0
visited = [[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if board[i][j]=='M': mx,my = i,j
        elif board[i][j]=='Z': zx,zy = i,j

bfs(mx,my,[0,1,2,3])
bfs(zx,zy,[0,1,2,3])

# 아직 가스관 설치 전이므로 M~Z 사이는 떨어져 있을 수 있음
# 따라서, 가스관이 설치되어 있는데 bfs로 방문 한 기록이 없을 경우 bfs 실행
for i in range(r):
    for j in range(c):
        if board[i][j]!='.' and not visited[i][j]:
            bfs(i,j,getDir(board[i][j]))

if len(pipeList) == 4: print(px,py,'+')
else:
    block = ['|', '-', '1', '2', '3', '4']
    pipeList.sort()
    # 파이프를 하나씩 대조해보면서 구한 이동방향과 맞는지 확인
    for b in block:
        if pipeList == getDir(b):
            print(px,py,b)