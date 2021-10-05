# 마법사 상어와 블리자드
from collections import deque

bdx = [-1,1,0,0]
bdy = [0,0,-1,1]
edx = [0,1,0,-1]
edy = [-1,0,1,0]
edx2 = [1,0,-1,0]
edy2 = [0,1,0,-1]

# 블리자드 마법으로 구슬 파괴
def breakBalls(dir,num):
    nx,ny = sx,sy

    for i in range(num):
        nx,ny = nx+bdx[dir],ny+bdy[dir]
        board[nx][ny] = 0

# 구슬 이동
def moveBalls():
    q,blankQ = deque(),deque()
    q.append([sx,sy])
    cnt = 1

    # 큰 회전 횟수 (상하좌우 한 바퀴)
    for k in range(n//2+1):
        # 상하좌우 이동
        for i in range(4):
            x,y = q.popleft()
            nx,ny = x,y
            for j in range(cnt):
                nx,ny = nx+edx[i],ny+edy[i]
                if 0<=nx<n and 0<=ny<n:
                    if board[nx][ny] == 0:
                        blankQ.append([nx,ny])
                    elif blankQ:
                        bx,by = blankQ.popleft()
                        board[bx][by] = board[nx][ny]
                        board[nx][ny] = 0
                        blankQ.append([nx,ny])
            q.append([nx,ny])
            if i%2==1: cnt+=1
            if k==n//2 and i==1: break

# 구슬 폭발
def exploreBalls():
    global result

    q,exBalls,explore = deque(),deque(),[[sx,sy-1]] # exBalls : 폭발 될 구슬 저장
    q.append([sx, sy-1])
    cnt,num,flag = 1,board[sx][sy-1],0

    # 큰 회전 횟수 (상하좌우 한 바퀴)
    for k in range(n // 2):
        # 상하좌우 이동
        for i in range(4):
            if q:
                x, y = q.popleft()
                nx, ny = x, y
                for j in range(cnt):
                    nx,ny = nx+edx2[i],ny+edy2[i]
                    if board[nx][ny] == 0: flag=1; break

                    if 0<=nx<n and 0<=ny<n:
                        if board[nx][ny] == num:
                            explore.append([nx,ny])
                        else:
                            if len(explore)>3: exBalls.append(explore)
                            explore = [[nx,ny]]
                            num = board[nx][ny]
                if flag: break
                if board[nx][ny]!=0: q.append([nx, ny])
                if cnt==1: cnt+=1
                elif i%2==0: cnt+=1
            else: flag=1; break
        if flag: break

    if len(explore)>3: exBalls.append(explore)
    if not exBalls: return 0

    # 4개 이상 연속한 구슬들 폭발
    for exp in exBalls:
        num = board[exp[0][0]][exp[0][1]]
        result += num * (len(exp))
        for i in range(len(exp)):
            board[exp[i][0]][exp[i][1]] = 0
    return 1

# 구슬 변화
def changeBalls():
    q =deque()
    q.append([sx, sy-1])
    num,numCnt,cnt = board[sx][sy-1],1,1
    change = deque()

    # 큰 회전 횟수 (상하좌우 한 바퀴)
    for k in range(n // 2):
        # 상하좌우 이동
        for i in range(4):
            x, y = q.popleft()
            nx, ny = x, y
            for j in range(cnt):
                nx,ny = nx+edx2[i],ny+edy2[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == num:
                        numCnt += 1
                    else:
                        change.append(numCnt)
                        change.append(num)
                        num,numCnt = board[nx][ny],1
            q.append([nx, ny])
            if cnt == 1:
                cnt += 1
            elif i % 2 == 0:
                cnt += 1

    q = deque()
    q.append([sx, sy])
    cnt,flag = 1,0

    # 변화한 구슬로 재 배치
    for k in range(n // 2 + 1):
        for i in range(4):
            x, y = q.popleft()
            nx, ny = x, y
            for j in range(cnt):
                nx, ny = nx + edx[i], ny + edy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if change:
                        ch = change.popleft()
                        board[nx][ny] = ch
                    elif board[nx][ny]!=0:
                        board[nx][ny] = 0
                    else:
                        flag = 1
                        break
            if flag: break
            q.append([nx, ny])
            if i % 2 == 1: cnt += 1
            if k == n // 2 and i == 1: break
        if flag: break

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
magic = [list(map(int,input().split())) for _ in range(m)]
sx,sy,result = n//2,n//2,0
for mag in magic:
    # 블리자드 마법으로 구슬 파괴
    breakBalls(mag[0]-1,mag[1])

    while True:
        # 구슬 이동
        moveBalls()
        # 구슬 폭발
        flag = exploreBalls()
        if not flag: break

    # 구슬 변화
    changeBalls()
print(result)