#소문난 칠공주
'''
좌표 기준(x,y)만으로 탐색 하면 안됨! => 탐색 안되는 곳 존재
(ex: 십자가 모양)
    YYSYY
    SSSSS
    YYSYY
    YYYYY
    YYYYY

갈 수 있는 위치 모두 possible 리스트에 저장 후,
possible에 있는 좌표 princess에 하나씩 추가하며 탐색
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(n,cnt):
    # 남은 만큼 (7-n) 더 루프를 돌아도 cnt>=4 되는 것이 불가능
    if cnt+(7-n)<4: return

    if n==7:
        if cnt>=4:
            temp=list(princess)
            temp.sort()
            temp=tuple(temp)
            result.add(temp)
        return

    possible=set()
    for x,y in princess:
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            # 갈 수 있는 곳 모두 possible에 저장
            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
                possible.add((nx,ny))

    # possible에 있는 (x,y)를 하나씩 선택하면서 dfs 탐색
    for x,y in possible:
        visited[x][y]=1
        princess.append((x,y))
        if board[x][y]=='S': dfs(n+1,cnt+1)
        else: dfs(n+1,cnt)
        princess.pop()
        visited[x][y]=0

board=[list(sys.stdin.readline().strip()) for _ in range(5)]
princess=deque()
result=set()
visited=[[0]*5 for _ in range(5)]

for i in range(5):
    for j in range(5):
        if board[i][j]=='S':
            visited[i][j]=1
            princess.append((i,j))
            dfs(1,1)
            princess.popleft()
print(len(result))