#다리 만들기2
'''
1. 섬에 0번부터 라벨링 해주기
2. 모든 섬의 영역을 dfs로 탐색하면서 다리 길이 저장
    2-1) 범위를 벗어나면 중단
    2-2) 자기 자신의 섬을 만나면 중단
    2-3) 다리가 1인 경우 중단
    2-4) 다른 섬을 만나면 다리의 길이 bridgeLength 리스트에 저장
3. 섬과 연결 된 다른 섬들을 linkedIsland 리스트에 저장 (i번째 섬과 j번,k번째 섬이 연결 됨..)
   섬과 섬을 연결하는 다리 번호를 0번부터 linkedBridge 리스트에 저장 (0번 섬과 1번 섬은 0번 다리로 연결되어 있다...)
4. 섬의 개수//2 (or 섬의 개수//2+1) ~ 섬의 개수만큼 i개 선택 (다리를 몇 개 놓을지)
   4-1) 다리의 개수가 i개가 될 때까지 selectedBridge 리스트에서 다리 선택 (0번 다리, 1번 다리,...)
   4-2) 다리의 개수 == i이면, 선택한 다리로 갈 수 있는 섬 탐색
        선택한 다리여야 하고, 방문하지 않은 섬이라면 islandCnt+=1
        islandCnt == 섬의 개수이면 모든 섬을 방문 할 수 있는 것
5. 모든 섬을 방문 할 수 있다면 다리의 최소 길이 구하기

처리해줘야 할 게 많아서 시간도 많이 걸리고 너어어무 어려웠다 ^.ㅜ..
혼자서는 못 풀겠어서 구글 풀이 참고
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 섬에 번호 붙이기
def labeling(x,y,number):
    q=deque()
    q.append([x,y])
    board[x][y]=number
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and initBoard[nx][ny]==1 and board[nx][ny]==-1:
                board[nx][ny]=number
                q.append([nx,ny])

# 섬의 한 지점에서 다른 섬을 만날 때까지 dfs로 탐색 + 다리 길이 구하기
def dfs(x,y,dir,dist,start):
    nx,ny=x+dx[dir],y+dy[dir]
    if not 0<=nx<n or not 0<=ny<m:
        return
    # 섬을 만난 경우
    if board[nx][ny]!=-1:
        end = board[nx][ny]
        # 자신의 섬을 만나면 return
        if start==end: return
        if dist==1: return
        bridgeLength[start][end]=min(dist,bridgeLength[start][end])
        return
    dfs(nx,ny,dir,dist+1,start)

# 다리 선택 후 모든 섬이 이어져 있는지 확인 + 최소 다리 길이 구하기
def findMinBridgeLenth(cnt,idx,limit):
    global result
    # 다리를 limit개 선택 했다면, 모든 섬이 연결 됐는지 확인
    if cnt==limit:
        q=deque()   # 방문 할 섬 저장
        visited=[0]*number

        islandCnt,totalLength=1,0    # 이어진 섬의 개수, 다리 길이의 총 합
        for i in range(number):
            if not visited[i]:
                q.append(i)
                visited[i]=1
                while q:
                    x=q.popleft()
                    # 연결 된 섬 탐색
                    for nx in linkedIsland[x]:
                        # 선택 한 다리이고, 방문하지 않은 섬이라면
                        if selectedBridge[linkedBridge[x][nx]] and visited[nx]==0:
                            islandCnt+=1
                            visited[nx]=1
                            q.append(nx)
                            totalLength+=bridgeLength[x][nx]

        if islandCnt==number:
            result=min(result,totalLength)
            return

    # 사용 할 다리 선택
    for i in range(idx,bridgeNum):
        selectedBridge[i]=1
        findMinBridgeLenth(cnt+1,i+1,limit)
        selectedBridge[i]=0


n,m=map(int,sys.stdin.readline().split())
initBoard=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
board=[[-1]*m for _ in range(n)]    # 라벨링 된 섬 0번 ~ i번까지 저장

# 섬에 번호 붙이기 (0번 ~ i번)
number=0
for i in range (n):
    for j in range(m):
        if initBoard[i][j] and board[i][j]==-1:
            labeling(i,j,number)
            number+=1

# 섬 number의 모든 지점에서 dfs 탐색
bridgeLength=[[10]*number for _ in range(number)]     # i섬과 j섬 사이에 연결 된 다리 길이 저장
for i in range(n):
    for j in range(m):
        if initBoard[i][j]:
            for k in range(4):
                dfs(i,j,k,0,board[i][j])     # (x, y, 방향, 다리 길이, 시작 섬 번호)

linkedIsland=[[] for _ in range(number)]    # 몇 번째 섬과 몇 번째 섬이 연결되어 있는지 저장
linkedBridge=[[-1]*number for _ in range(number)]   # 두 섬을 연결 한 다리 번호 저장
bridgeNum=0
for i in range(number-1):
    for j in range(i+1,number):
        if bridgeLength[i][j]<10:
            linkedIsland[i].append(j)
            linkedIsland[j].append(i)
            linkedBridge[i][j]=bridgeNum
            linkedBridge[j][i]=bridgeNum
            bridgeNum+=1

selectedBridge=[0]*bridgeNum    # 선택 된 다리 저장
# 선택 할 다리 최소 개수 구하기
if number%2==0: start=number//2
else: start=(number//2)+1
result=int(1e9)
# 다리를 i개 선택 후, 최소 다리 길이 구하기
for i in range(start,bridgeNum+1):
    findMinBridgeLenth(0,0,i)

if result==int(1e9): print(-1)
else: print(result)