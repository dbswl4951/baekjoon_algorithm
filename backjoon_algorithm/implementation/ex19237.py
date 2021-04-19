#어른 상어
'''
1차 시도 때 시간초과 원인은 아마
    1) 갈 수있는 모든 경로를 탐색 후 배열에 저장하고,
    2) 그 배열에서 우선순위가 가장 높은 애를 뽑아내서 인 듯 하다.
즉, 처음부터 우선 순위가 제일 높은 애만 찾는 것이 아니라, 모든 칸을 다 찾기 때문에 시간 오래 걸렸음!!

2차 시도 풀이에선
우선 순위에 따라 상하좌우 탐색 후, 갈 수 있는 곳이 있으면 break로 그 이후 탐색은 수행하지 X
'''

dx=[0,-1,1,0,0]
dy=[0,0,0,-1,1]

n,m,k=map(int,input().split())
# board: [상어 번호, k], shark: [x, y, 방향]
board,shark=[],[[] for _ in range(m)]
for i in range(n):
    board.append(list(map(int,input().split())))
    for j in range(n):
        if board[i][j]:
            shark[board[i][j]-1].extend([i,j])
            board[i][j]=[board[i][j],k]
sDir=list(map(int,input().split()))
for i in range(m):
    shark[i].append(sDir[i])
# 방향 우선순위 입력
priority=[]
for i in range(m):
    priority.append([list(map(int,input().split())) for _ in range(4)])

result=0
while True:
    result+=1
    if result==1001:
        print(-1)
        break

    check=[[0]*n for _ in range(n)]     # 상어 중복 체크하기 위해서, 상어 번호 저장
    # 상어 마리 수 만큼
    for i in range(m):
        if shark[i]:
            x,y,dir,flag=shark[i][0],shark[i][1],shark[i][2],0    # flag: 다음 칸이 빈 칸인지 아닌지
            # 우선 순위에 따라 갈 수 있는 칸 탐색 => 찾으면 break
            for j in range(4):
                d=priority[i][dir-1][j]
                nx,ny=x+dx[d],y+dy[d]
                if 0<=nx<n and 0<=ny<n:
                    if board[nx][ny]==0:
                        flag=1  # 다음 갈 수 있는 칸이 빈 칸
                        break
            # 다음 갈 수 있는 칸이 빈 칸이 아니라면, 자기 냄새 칸 찾아서 이동
            if not flag:
                for j in range(4):
                    d=priority[i][dir-1][j]
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny][0]==i+1: break

            # 해당 좌표에 다른 상어가 있다면 번호 큰 상어 삭제
            if check[nx][ny]:
                if check[nx][ny]<i+1: shark[i]=0
                else: shark[check[nx][ny]-1]=0
            else:
                check[nx][ny]=i+1
                shark[i]=[nx,ny,d]

    # 냄새 유지 시간-=1
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                board[i][j][1]-=1
                if board[i][j][1]==0: board[i][j]=0

    # 이동 한 상어 board에 표시
    for i in range(m):
        if shark[i]:
            board[shark[i][0]][shark[i][1]]=[i+1,k]
    # 상어가 한 마리만 남으면 종료
    if shark.count(0)==m-1:
        print(result)
        break


# 1차 시도 => 시간 초과
'''
from collections import deque

dx=[0,-1,1,0,0]
dy=[0,0,0,-1,1]

# 이동 가능 한 곳 return
def bfs(num,x,y):
    noSmell,mySmell=[],[]
    for i in range(1,5):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            # 빈 칸인 경우
            if board[nx][ny]==0:
                noSmell.append([i,nx,ny])
            # 자신의 냄새 칸인 경우
            elif board[nx][ny][0]==num:
                mySmell.append([i,nx,ny])
    if noSmell: return noSmell,1
    return mySmell,0

# 냄새 시간 1초씩 감소
def disappearSmell():
    idx = 0
    while idx < len(smell):
        smell[idx][0] -= 1
        if smell[idx][0] == 0:
            smell.popleft()
        else:
            idx += 1
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                board[i][j][1] -= 1
                if board[i][j][1]==0:
                    board[i][j]=0

# 냄새 퍼트리기
def spreadSmell(spread):
    for num, x, y,nx,ny in spread:
        if board[nx][ny]==0 or (board[nx][ny] and board[nx][ny][0]>num):
            board[nx][ny] = [num, k]
        if [k,nx,ny] not in smell:
            smell.append([k, nx, ny])
    return smell

# 한 칸에 여러마리 있는지 확인 후, 상어 내쫓기
def check():
    global sharks
    delete=[]
    for i in range(len(sharks)):
        for j in range(i+1,len(sharks)):
            if sharks[i][1]==sharks[j][1] and sharks[i][2]==sharks[j][2]:
                if sharks[i][0]>sharks[j][0]: delete.append(sharks[i])
                else: delete.append(sharks[j])
    # 상어 삭제
    for d in delete:
        idx=0
        while idx<len(sharks):
            if d[0]==sharks[idx][0]:
                del sharks[idx]
                break
            else: idx+=1

# 상어 옮기기
def moveSharks():
    global result,sharks

    while result<=1000:
        sLen=len(sharks)
        result+=1
        spread=[]

        # 상어 마리 수 만큼
        while sLen:
            num,x,y,dir=sharks.popleft()
            # 상어가 이동 가능한 곳 찾기 (case=0: 빈칸으로 이동, case=1: 자신의 냄새 칸으로 이동)
            ableMove,case=bfs(num,x,y)
            # 이동 가능한 칸이 여러개면 우선순위에 따라 이동
            if len(ableMove)>1:
                flag=0
                d,ax,ay=0,0,0
                for p in priority[num-1][dir-1]:
                    for i in range(len(ableMove)):
                        if p==ableMove[i][0]:
                            d,ax,ay=ableMove[i]
                            if case==0:
                                board[ax][ay]=[num,k+1]
                            flag=1
                            break
                    if flag: break
            else:
                d,ax,ay=ableMove[0]
                if case == 0:
                    board[ax][ay] = [num, k+1]
            sharks.append([num,ax,ay,d])
            spread.append([num,x,y,ax,ay])
            sLen-=1

        disappearSmell()
        # 한 칸에 여러마리 상어 있는지 체크 => 있으면 내쫓기
        check()
        # 1번 상어만 남았는지 체크
        if len(sharks) == 1 and sharks[0][0] == 1: break
        # 냄새 뿌리기
        smell = spreadSmell(spread)

n,m,k=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
sDir=list(map(int,input().split()))
sharks,smell=deque(),deque()
for i in range(n):
    for j in range(n):
        if board[i][j]>0:
            sharks.append([board[i][j],i,j,sDir[board[i][j]-1]])  # (상어번호, x, y, 방향)
            board[i][j]=[board[i][j],k] # 냄새 뿌리기
            smell.append([k,i,j])
priority=[]
for i in range(m):
    priority.append([list(map(int,input().split())) for _ in range(4)])
result=0
moveSharks()
if result==1001: print(-1)
else: print(result)
'''