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

def bfs(board,visited,q):
    global result
    count=0

    while q:
        qLen=len(q)
        red=set()
        green=set()
        while qLen:
            x, y = q.popleft()
            print("x,y:",x,y)
            # 이미 꽃 피운 자리는 넘어가기
            if not board[x][y]: continue
            color=board[x][y]

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny] and not visited[nx][ny]:
                    print("nx,ny:",nx,ny)
                    if (color==3 and (nx,ny) in red) or (color==4 and (nx,ny) in green):
                        count+=1
                        board[nx][ny]=0
                        print("c:",count)
                        print("board:",board)
                    else:
                        board[nx][ny]=board[x][y]
                        q.append([nx,ny])
                        print("board:",board)
                        print("q:",q)
                        if board[nx][ny]==3: green.add((nx,ny));print("green:",green)
                        else: red.add((nx,ny));print("red:",red)
            qLen-=1
            for gx,gy in green:
                if not visited[gx][gy]: visited[gx][gy] = 1
            for rx,ry in red:
                if not visited[rx][ry]: visited[rx][ry] = 1
    print("count====",count)
    result=max(result,count)

n,m,g,r=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
able=[]
for i in range(n):
    for j in range(m):
        if board[i][j]==2: able.append([i,j])

result=0
for case in combinations(able,g+r):
    print("case:",case)
    # 초록색 배양액 선택
    for select in combinations(case,g):
        print("select:",select)
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
        print(copyBoard)
        bfs(copyBoard,visited,q)
print(result)