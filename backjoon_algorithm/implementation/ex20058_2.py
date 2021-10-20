#마법사 상어와 파이어스톰
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 시계방향으로 90도 회전
def rotate(x,y,l):
    temp = [[0]*l for _ in range(l)]

    # board를 위쪽으로 읽고, temp에 -> 쪽으로 쓴다
    for i in range(l):
        for j in range(l):
            temp[i][j] = board[x+l-1-j][y+i]
    # board에 회전된 값이 들어있는 temp를 다시 쓴다
    for i in range(l):
        for j in range(l):
            board[x+i][y+j] = temp[i][j]

# 인접한 면 체크 후, 얼음 -1
def check(x,y):
    cnt = 0

    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n and board[nx][ny]!=0: cnt+=1
    # 주의! 면이 2개 이하임을 발견하고 바로 얼음을 빼주면 안됨
    # 얼음을 뺀 순간 0이 되서 없어질 경우, 다른 칸에 영향을 줄 수 있음
    if cnt<3: return 1
    return 0

# 가장 큰 얼음 덩어리 찾기
def bfs(x,y):
    global iceCount

    q = deque()
    q.append([x,y])
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    cnt = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[nx][ny]!=0:
                visited[nx][ny] = 1
                cnt += 1
                q.append([nx,ny])
    iceCount = max(iceCount,cnt)

n,q = map(int,input().split())
n = 2**n
board = [list(map(int,input().split())) for _ in range(n)]
levels = list(map(int,input().split()))
sumIce,iceCount = 0,0

for level in levels:
    l = 2**level
    melting = []

    # 시계 방향으로 90도 회전
    for i in range(0,n,l):
        for j in range(0,n,l):
            rotate(i,j,l)

    # 인접한 면 체크 후, 얼음 -1
    for i in range(n):
        for j in range(n):
            if board[i][j]!=0:
                if check(i,j):
                    melting.append([i,j])
    for mx,my in melting:
        board[mx][my] -= 1

# 얼음의 합, 가장 큰 얼음 덩어리 찾기
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            sumIce += board[i][j]
            bfs(i,j)
print(sumIce)
print(iceCount)