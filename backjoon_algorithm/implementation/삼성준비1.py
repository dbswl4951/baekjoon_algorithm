#동전 챙기기
'''
1. 수집 할 동전 3개 선택
    => 삼성은 itertools 사용 불가! dfs로 구현하는 법 알아두자!
2. 선택 된 동전에 대해 BFS로 최소 경로 탐색
 이 때, 동전의 위치에 따라 총 4번으로 나눠서 BFS 실행
    => 간 곳을 또 갈 수 있기 때문
'''
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def getMoveCnt(start,end):
    q=deque()
    x,y=start
    q.append([x,y])
    visited = [[0] * n for _ in range(n)]
    visited[x][y]=1
    move = [[0] * n for _ in range(n)]

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[nx][ny]!='#':
                visited[nx][ny]=1
                move[nx][ny]=move[x][y]+1
                q.append([nx,ny])
            if nx==end[0] and ny==end[1]: break

    if visited[end[0]][end[1]]==0: return -1
    return move[end[0]][end[1]]

# 뽑은 동전을 지나는 최소 경로 구하기
def getTotalMoveCnt():
    totalCnt=0
    # 시작~첫번째 동전, 첫번째 동전~두번째, 두번째~세번째, 세번째~도착지 => 총 4번 수행
    for i in range(4):
        start=[sx,sy] if i==0 else coins[selected[i-1]]
        end=[ex,ey] if i==3 else coins[selected[i]]
        cnt=getMoveCnt(start,end)

        if cnt==-1: return -1
        totalCnt+=cnt
    return totalCnt

# 동전 3개 뽑기
def dfs(idx,cnt):   # idx : 뽑을 동전 인덱스, cnt : 동전 몇 개 뽑았는지
    global result

    # 3개의 동전을 뽑았으면, 최소 경로 구하기
    if cnt==3:
        moveCnt=getTotalMoveCnt()
        if moveCnt==-1: return
        result=min(result,moveCnt)
        return

    if idx==len(coins):
        return

    selected.append(idx)
    dfs(idx+1,cnt+1)
    selected.pop()
    dfs(idx+1,cnt)

n=int(input().strip())
board=[list(input().strip()) for _ in range(n)]
coins,selected=[],[]    # coin:모든 동전 위치 저장, selected:선택한 동전
sx,sy,ex,ey=0,0,0,0
for i in range(n):
    for j in range(n):
        if board[i][j]=='S':
            sx,sy=i,j
        elif board[i][j]=='E':
            ex,ey=i,j
        elif board[i][j].isdigit():
            coins.append([i,j])

result=int(1e9)
# 가능한 모든 동전 조합 찾기
dfs(0,0)
if result==int(1e9): print(-1)
else: print(result)