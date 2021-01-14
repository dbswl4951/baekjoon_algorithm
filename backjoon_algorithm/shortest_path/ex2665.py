#미로 만들기
'''
bfs + dp
검은 방 개수 구하는게 잘 안되서 힌트 참고
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    visited[0][0]=0
    q=deque()
    q.append([0,0])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny]==-1: #한 번도 방문 하지 않았을 때
                    if room[nx][ny]==0: #검은 방
                        visited[nx][ny]=visited[x][y]+1 #지나 온 검은 방 수 +1
                        q.append([nx,ny])
                    else:   #흰 방
                        visited[nx][ny]=visited[x][y]
                        #흰 방을 우선적으로 방문해야 바꿔야 하는 검은방의 최소값 구할 수 있으로 queue의 왼쪽에 값 삽입
                        q.appendleft([nx,ny])

n=int(sys.stdin.readline().strip())
room=[]
for _ in range(n):
    room.append(list(map(int,sys.stdin.readline().strip())))
visited=[[-1]*n for _ in range(n)]  #방문여부, 지나 온 검은 방 개수 구하기 위해 선언
bfs()
print(visited[n-1][n-1])