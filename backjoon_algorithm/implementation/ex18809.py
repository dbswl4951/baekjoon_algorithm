#Gaaaaaaaaaarden
'''
1. 초록색 배양액, 빨간색 배양액 뿌릴 곳 선택해서 뿌리기 (초록색:3, 빨간색:4)
2. bfs로 초록색, 빨간색 배양액 퍼트리기
3. 초록색, 빨간색 만난다면
'''
import sys,copy
from itertools import combinations
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(board,case,green):
    count=0
    greenQ,redQ=deque(),deque()

    # 초록색, 빨간색 배양액 큐에 넣기
    for x,y in case:
        if [x,y] in green: greenQ.append([x,y])
        else: redQ.append([x,y])

    while greenQ:
        # 한 턴마다의 결과 저장
        greenSet,redSet=set(),set()
        while greenQ:
            x,y=greenQ.popleft()
            board[x][y]=3
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if board[nx][ny]==1 or board[nx][ny]==2: greenSet.add((nx,ny))
        while redQ:
            x,y=redQ.popleft()
            board[x][y]=4
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if board[nx][ny]==1 or board[nx][ny]==2: redSet.add((nx,ny))

        inter=greenSet&redSet
        greenSet=greenSet-inter
        redSet=redSet-inter
        # 교집합은 배양액끼리 만난 곳 => 꽃 피우기
        for x,y in inter:
            count+=1
            board[x][y]=5
        for x,y in greenSet: board[x][y]=3
        for x,y in redSet: board[x][y]=4

        greenQ.extend(greenSet)
        redQ.extend(redSet)
    return count

n,m,g,r=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
able=[]
for i in range(n):
    for j in range(m):
        if board[i][j]==2: able.append([i,j])

result=0
for case in combinations(able,g+r):
    # 초록색 배양액 선택
    for green in combinations(case,g):
        copyBoard=copy.deepcopy(board)
        result=max(result,bfs(copyBoard,case,green))
print(result)


# 1차 시도 => 시간 초과
'''
import sys,copy
from itertools import combinations
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(board,q,visited):
    global result
    count=0
    while q:
        qLen=len(q)
        # 배양액이 합쳐 질 수 있는 곳 저장
        visitSet = set()
        
        while qLen:
            x,y=q.popleft()
            if board[x][y]==0: qLen-=1; continue
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]!=0 and not visited[nx][ny]:
                    if (nx,ny) in visitSet and board[nx][ny]!=board[x][y]:
                        count+=1
                        board[nx][ny]=0
                    else:
                        visitSet.add((nx,ny))
                        board[nx][ny]=board[x][y]
                        q.append([nx,ny])
            qLen -= 1

        for vx,vy in visitSet:
            if board[vx][vy]!=0:
                visited[vx][vy]=1
    result=max(result,count)

n,m,g,r=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
able=[]
for i in range(n):
    for j in range(m):
        if board[i][j]==2: able.append([i,j])

result=0
for case in combinations(able,g+r):
    # 초록색 배양액 선택
    for select in combinations(case,g):
        q=deque()
        copyBoard=copy.deepcopy(board)
        visited = [[0] * m for _ in range(n)]
        for s in select:
            copyBoard[s[0]][s[1]]=3
            q.append([s[0],s[1]])
            visited[s[0]][s[1]]=1
        # 남은 곳에 빨간색 배양액 뿌리기
        for c in case:
            if copyBoard[c[0]][c[1]]!=3:
                copyBoard[c[0]][c[1]]=4
                q.append([c[0], c[1]])
                visited[c[0]][c[1]]=1
        bfs(copyBoard,q,visited)
print(result)
'''