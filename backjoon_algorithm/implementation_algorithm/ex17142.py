#연구소3
'''
1. 바이러스를 퍼트릴 m개 좌표 선택
 1-1) 남은 바이러스 자리는 벽으로 생각 (1로 변경)
2. bfs 사용 => 상하좌우 퍼트리기
'''
import sys,copy
from collections import deque
from itertools import combinations

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#바이러스 퍼트리기
def bfs(case):
    tempBoard=copy.deepcopy(board)
    global result
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    #바이러스 있는 곳은 -1로 설정
    for x,y in case:
        tempBoard[x][y]=-1
        q.append([x,y])
        visited[x][y]=0
    second = 0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1 and tempBoard[nx][ny]!=1:
                visited[nx][ny] = visited[x][y] + 1
                #빈 칸일때만 (비활성 바이러스는 초 갱신X)
                if tempBoard[nx][ny]==0:
                    #몇 초 걸렸는지 갱신
                    second=max(m,visited[nx][ny])
                q.append([nx,ny])
    #2차원 배열 => 이어붙인 1차원 배열로 변경
    temp=list(sum(visited,[]))
    #방문 안한 곳이 벽의 개수와 동일 한지 (벽만 빼고 다 방문했는지 체크)
    if temp.count(-1)==list(sum(tempBoard,[])).count(1):
        result.append(second)

n,m=map(int,sys.stdin.readline().split())
board=[]
virus=deque()
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))
    for j in range(n):
        if board[i][j]==2:
            virus.append([i,j])
result=[]
#높을 수 있는 모든 바이러스 위치 설정
for case in combinations(virus,m):
    bfs(case)
print(min(result) if result else -1)