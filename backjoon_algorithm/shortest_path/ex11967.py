#불켜기
'''
불 키기를 체크하는 건 2가지 경우가 발생했을 때임
1) 현재 위치(x,y)에서 다른 위치(cx,cy)의 불을 키고, 불을 킨 위치의 상하좌우 중 방문 한 적이 있는 곳
    => (cx,cy)에 불을 킴으로써, 다른 경로로 이동 가능 할수도 있기 때문에 (cx,cy)의 상하좌우를 큐에 넣어준다
2) 현재 위치(x,y)의 상하좌우 중 방문 한 적 없고, 불이 켜져 있는 곳
'''
import sys
from collections import deque,defaultdict

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def turnOn():
    q=deque()
    q.append((0,0))
    visited=[[0]*n for _ in range(n)]
    visited[0][0]=1
    check = [[0] * n for _ in range(n)]
    check[0][0] = 1
    result=1

    while q:
        x,y=q.popleft()
        for cx,cy in board[(x,y)]:
            if not check[cx][cy]:
                result+=1
                check[cx][cy]=1
                # 불 킨 방 상하좌우 중 방문했던 곳(도달 가능한 곳)은 큐에 삽입
                # => 현재 내 위치와 떨어져있지만, 불 킨 방의 상하좌우를 통해 다른 방으로 이동 할 수 있으므로 재검사 해야 함
                for i in range(4):
                    cnx,cny=cx+dx[i],cy+dy[i]
                    if 0<=cnx<n and 0<=cny<n and visited[cnx][cny]:
                        q.append((cnx,cny))

        # 현재 위치와 인접한 곳 중, 방문하지 않았고 불이 켜져있으면 이동가능하므로 큐에 삽입
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0 <=nx< n and 0 <=ny< n and not visited[nx][ny] and check[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))
    return result

n,m=map(int,sys.stdin.readline().split())
board=defaultdict(list)
for _ in range(m):
    a,b,c,d=map(int,sys.stdin.readline().split())
    board[(a-1,b-1)].append((c-1,d-1))
print(turnOn())