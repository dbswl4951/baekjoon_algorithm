#상어 중학교
'''
2021 삼성 상반기 오전 문제

검은색 : -1
무지개 : 0
일반 : M이하의 자연수

- 블록 그룹엔 일반 블록이 하나 이상 있어야 함
- 일반 블록의 색은 모두 같아야 함
- 검은색 블록 포함 되면 X
- 무지개 블록 개수 상관 X
- 블록은 2개 이상

< 블록 그룹이 존재 하는 동안 계속 반복 >
< 최종 점수 구하기 >
1. 크기가 가장 큰 블록 그룹 찾기 (bfs)
  1) 크기가 같은 그룹이 여러개라면, 무지개 블록 수가 많은 그룹
  2) (1)이 여러개라면, 기준 블록 행이 가장 큰 것
  3) (2)가 여러개라면, 기준 블록 열이 가장 큰 것
    * 기준 블록 : 무지개 블록이 아닌 블록 중, 행/열이 가장 작은 것
2. 블록 그룹 제거 (B개)
3. B^2 점수 +
4. 검은 블록 제외, 모든 블록이 아래로 이동
5. 90도 반시계 방향 회전
6. 4번 반복
'''
from collections import deque
import copy

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 블록 그룹 구하기
def grouping(x,y):
    sx,sy=21,21   # 기준 블록
    color,nomalCnt=-1,0    # 일반 블록 색, 개수
    blockGroup=[]
    check=[[0]*n for _ in range(n)]
    check[x][y]=1

    if board[x][y]>0:
        sx,sy=x,y
        color=board[x][y]
        nomalCnt+=1
        blockGroup.append([color,x,y])
    q=deque()
    q.append([x,y])

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not check[nx][ny] and board[nx][ny]>-1:
                # 일반 블록 만남
                if board[nx][ny]>0:
                    if color==-1:
                        color=board[nx][ny]
                    elif color!=board[nx][ny]: continue
                    # 기준 블록 갱신
                    if nx<sx or (nx==sx and ny<sy):
                        sx, sy = nx, ny
                    nomalCnt+=1
                    visited[nx][ny] = 1

                check[nx][ny] = 1
                q.append([nx, ny])
                blockGroup.append([board[nx][ny], nx, ny])

    if len(blockGroup)>=2 and nomalCnt>=1:
        return blockGroup,sx,sy
    return None,None,None

# 블록 그룹 제거
def deleteBolckGroup(blockGroup):
    global score
    bLen=len(blockGroup)
    for num,x,y in blockGroup:
        board[x][y]=-2
    # 점수 증가
    score+=bLen*bLen

# 검은 블록 제외, 모든 블록 아래로 이동
def moveDown(board):
    for j in range(n):
        high,top=0,n
        for i in range(n-1,-1,-1):
            if board[i][j]==-2:
                high+=1
            elif board[i][j]==-1:
                top=i
                high=0
            else:
                if top-1==i:
                    top-=1
                    continue
                elif top!=n:
                    board[i+high][j]=board[i][j]
                else:
                    board[top-1][j]=board[i][j]
                    top-=1
                board[i][j] = -2
    return board

# 반시계 방향으로 90도 회전
def rotate270(board):
    temp=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[n-1-j][i]=board[i][j]
    return temp

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
score=0

while True:
    visited = [[0] * n for _ in range(n)]
    maxBlockGroup,x,y = [],-1,-1  # 삭제 할 블록 그룹, 기준 x, 기준 y
    # 삭제 할 블록 그룹 찾기
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j]>-1:
                visited[i][j]=1
                blockGroup,sx,sy=grouping(i,j)
                if blockGroup!=None:
                    mbLen,bLen=len(maxBlockGroup),len(blockGroup)
                    # 크기, max 기준 행, max 기준 열 순으로 블록 찾아서 갱신
                    if mbLen<bLen or (mbLen==bLen and x<sx) or (mbLen==bLen and x==sx and y<sy):
                        maxBlockGroup=copy.deepcopy(blockGroup)
                        x,y=sx,sy

    if not maxBlockGroup: break

    # 블록 그룹 삭제 + 점수 증가 => 삭제 된 블록은 -2로 갱신
    deleteBolckGroup(maxBlockGroup)
    # 검은 블록 제외, 모든 블록 아래로 이동
    board=moveDown(board)
    # 반시계 방향으로 90도 회전
    board=rotate270(board)
    # 검은 블록 제외, 모든 블록 아래로 이동
    board=moveDown(board)

print(score)