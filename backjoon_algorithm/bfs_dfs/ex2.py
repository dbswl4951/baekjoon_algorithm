#미로 탈출
'''
최소 칸의 개수 => BFS(너비 우선 탐색) 사용
'''
from collections import deque

n,m=map(int,input().split())
maze=[]
for i in range(n):
    maze.append(list(map(int,input())))

#상,하,좌,우
directionX=[-1,1,0,0]
directionY=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append([x,y])
    while q:
        x,y=q.popleft()
        print("x,y:::::",x,y)
        for i in range(4):
            nx=x+directionX[i]
            ny=y+directionY[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny]==1: #괴물이 없는 부분을 방문하면 이전노드의 거리+1을 리스트에 넣음
                    q.append([nx,ny])
                    maze[nx][ny]=maze[x][y]+1
                    print("nx,ny:::",nx,ny)
                    print("maze------",maze)
    return maze[n-1][m-1]

print(bfs(0,0))