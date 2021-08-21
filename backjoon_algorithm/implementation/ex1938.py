#통나무 옮기기
import sys
from collections import deque

dx=[-1,1,0,0,1,1,-1,-1]
dy=[0,0,-1,1,1,-1,1,-1]

# 회전 가능한지 check 후, 회전
def checkTurn(tree):
    # 회전 확인은 중앙 기준으로, 대각선 4방향을 체크
    for i in range(4,8):
        nx,ny=tree[1][0]+dx[i], tree[1][1]+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=n or board[nx][ny]=='1': return

    x, y = tree[1][0], tree[1][1]
    # 가로 -> 세로 회전
    if tree[0][0]==tree[1][0]:
        if board[x-1][y]!='1' and board[x+1][y]!='1':
            nTree = [[x-1,y],[x,y],[x+1,y]]
            if nTree not in visited:
                visited.append(nTree)
                q.append(nTree)
    # 세로 -> 가로 회전
    else:
        if board[x][y-1]!='1' and board[x][y+1]!='1':
            nTree = [[x,y-1],[x,y],[x,y+1]]
            if nTree not in visited:
                visited.append(nTree)
                q.append(nTree)

def bfs():
    q.append(bTree)
    visited.append(bTree)
    result=0

    while q:
        qLen = len(q)
        while qLen:
            tree=q.popleft()
            if tree==eTree:
                print(result)
                return

            # 회전 가능한지 check 후, 회전
            checkTurn(tree)

            # 상하좌우 4방향 탐색
            for i in range(4):
                nTree=[]
                # 나무 3개 하나씩 옮기기
                for j in range(3):
                    nx,ny = tree[j][0]+dx[i], tree[j][1]+dy[i]
                    if 0<=nx<n and 0<=ny<n and board[nx][ny]!='1':
                        nTree.append([nx,ny])
                    else: break
                if len(nTree)==3 and nTree not in visited:
                    visited.append(nTree)
                    q.append(nTree)
            qLen-=1
        result+=1
    print(0)

n=int(sys.stdin.readline().strip())
board=[list(sys.stdin.readline().strip()) for _ in range(n)]
visited,bTree,eTree=[],[],[]
q = deque()
for i in range(n):
    for j in range(n):
        if board[i][j]=='B': bTree.append([i,j])
        elif board[i][j]=='E': eTree.append([i,j])
bfs()