#마법사 상어와 블리자드
'''
2021 삼성 상반기 오후 문제

1. d방향으로 s만큼 구슬 파괴
2. 빈 칸이 생기면, 구슬 앞으로 이동하며 빈 칸 채움
3. 같은 숫자 4개 이상 연속 => 폭발
4. (2) 실행
5. (3)과 (4) 반복 실행 (폭발 할 구슬이 없을 때 까지)
6. 구슬 그룹 (구슬의 개수, 구슬 번호)로 변경
7. (6) 과정에서 구슬이 칸의 개수보다 많아지면, 넘어간 구슬은 사라짐
<1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)>
'''
from collections import deque

# 마법 방향
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 구슬 이동 방향
mdx=[1,0,-1,0]
mdy=[0,1,0,-1]

# 마법으로 구슬 파괴하기
def useMagic(mag):
    d,s=mag
    x,y=sx,sy
    for _ in range(s):
        nx,ny=x+dx[d],y+dy[d]
        if 0<=nx<n and 0<=ny<n:
            board[nx][ny]=0
            x,y=nx,ny

# 빈 칸없게 구슬 이동
def moveBall():
    x,y=sx,sy-1
    moveCnt,addCnt=1,0   # 한 방향으로 이동 해야 할 횟수,
    empty=deque()   # 구슬 비어있는 칸 저장
    flag=0

    for _ in range(n//2+1):
        for i in range(4):
            for _ in range(moveCnt):
                if 0<=x<n and 0<=y<n:
                    if board[x][y]==0: empty.append([x,y])
                    nx,ny=x+mdx[i],y+mdy[i]
                    if 0<=nx<n and 0<=ny<n:
                        # 구슬 빈 칸으로 이동 시키기
                        if board[nx][ny]!=0 and empty:
                            ex,ey=empty.popleft()
                            board[ex][ey]=board[nx][ny]
                            board[nx][ny]=0
                    x,y=nx,ny
                else:
                    flag=1
                    break
            if flag: break
            addCnt+=1
            if addCnt%2!=0: moveCnt += 1
        if flag: break

# 같은 숫자 구슬 4개 이상이면 폭발 시키기
def explodeBall():
    x, y = sx, sy - 1
    moveCnt, addCnt = 1, 0  # 한 방향으로 이동 해야 할 횟수
    pathBall,beforeNum=[[x,y]],board[x][y]   # 연속된 구슬 저장, 전의 구슬 번호
    check=0  # 폭발이 일어났는지 체크
    flag=0

    for _ in range(n // 2 + 1):
        for i in range(4):
            for _ in range(moveCnt):
                if 0 <= x < n and 0 <= y < n:
                    nx,ny=x+mdx[i],y+mdy[i]
                    if 0<=nx<n and 0<=ny<n:
                        # 전의 구슬 번호와 같다면, 연속된 구슬 리스트(path)에 저장
                        if board[nx][ny]==beforeNum:
                            pathBall.append([nx,ny])
                        else:
                            # 그 전까지 연속 된 구슬이 4개 이상 있었다면 폭발 시키기
                            if len(pathBall)>=4:
                                for px,py in pathBall:
                                    board[px][py]=0
                                    check=1
                                    if 1<=beforeNum<=3:
                                        ball[beforeNum]+=1
                            beforeNum=board[nx][ny]
                            pathBall=[[nx,ny]]
                    x,y=nx,ny
                else:
                    flag=1
                    break
            if flag: break
            addCnt += 1
            if addCnt % 2 != 0: moveCnt += 1
        if flag: break
    return check

# 구슬 변화 시키기
def ballChange():
    x, y = sx, sy - 1
    moveCnt, addCnt = 1, 0  # 한 방향으로 이동 해야 할 횟수
    ballNum,ballCnt=board[x][y],1   # 구슬 번호, 구슬 개수
    newGroup=deque()    # 구슬 변환 후, board에 적용 할 새로운 구슬 정보
    flag=0

    for _ in range(n // 2 + 1):
        for i in range(4):
            for _ in range(moveCnt):
                if 0 <= x < n and 0 <= y < n:
                    nx, ny = x + mdx[i], y + mdy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if ballNum==board[nx][ny]:
                            ballCnt+=1
                        else:
                            newGroup.append(ballCnt)
                            newGroup.append(ballNum)
                            ballNum=board[nx][ny]
                            ballCnt=1
                    x, y = nx, ny
                else:
                    flag=1
                    break
            if flag: break
            addCnt += 1
            if addCnt % 2 != 0: moveCnt += 1
        if flag: break

    x, y = sx, sy - 1
    moveCnt, addCnt = 1, 0
    if newGroup: board[x][y]=newGroup.popleft()
    flag=0

    # 변화한 구슬 그룹 적용 시키기
    for _ in range(n // 2 + 1):
        for i in range(4):
            for _ in range(moveCnt):
                if 0 <= x < n and 0 <= y < n:
                    nx, ny = x + mdx[i], y + mdy[i]
                    if 0 <= nx < n and 0 <= ny < n and newGroup:
                        num=newGroup.popleft()
                        board[nx][ny]=num
                    x, y = nx, ny
                else:
                    flag=1
                    break
            if flag: break
            addCnt += 1
            if addCnt % 2 != 0: moveCnt += 1
        if flag: break


n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
sx,sy=n//2,n//2   # 상어 위치
magic=[]
for _ in range(m):
    d,s=map(int,input().split())
    magic.append([d-1,s])
bNum=0
for bo in board:
    for b in bo:
        bNum=max(bNum,b)
ball=[0]*4      # 폭발한 구슬 개수 저장

result=0
for i in range(m):
    # 마법으로 구슬 파괴하기
    useMagic(magic[i])
    # 빈 칸없게 구슬 이동
    moveBall()
    while True:
        # 같은 숫자 구슬 4개 이상이면 폭발 시키기
        flag=explodeBall()
        # 폭발이 일어나지 않으면 다음 단계로 넘어가기
        if not flag: break
        moveBall()
    # 구슬 변화 시키기
    ballChange()

for i in range(1,4):
    result+=i*ball[i]
print(result)