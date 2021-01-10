#내리막 길
'''
DFS + DP (Topdown방식)
visited[i][j]
    = 0 : 목적지까지 갈 수 있는 경로가 없으므로 0 반환
    = -1 : 방문하지 않은 경로이므로 정상적으로 DFS + DP 수행
    >=1 : 이전에 연산한 방문 경로가 있으므로 해당 값을 반환해서 더함

아직도 Topdown방식이 적응이 안된다ㅜ.ㅜ
'''
import sys
sys.setrecursionlimit(40000)

#2차 시도
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    if x==m-1 and y==n-1:
        return 1
    if visited[x][y]==-1:   # 아직 방문 하지 않은 곳이라면
        visited[x][y]=0
        #print("방문==",visited)
        for i in range(4):  #상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <=nx<m and 0 <=ny<n and area[nx][ny]<area[x][y]:
                #print("nx,ny:",nx,ny)
                visited[x][y]+=dfs(nx,ny)   # 이전에 연산한 방문 경로에 더해줌
                #print("visited::", visited)
    return visited[x][y]    #이미 방문한 곳은 저장 된 값 반환

m,n=map(int,sys.stdin.readline().split())
area=[]
for _ in range(m):
    area.append(list(map(int,sys.stdin.readline().split())))
visited=[[-1]*n for _ in range(m)]
print(dfs(0,0))


#1차 시도
'''
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    global visited
    if x == m - 1 and y == n - 1:
        return 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<m and 0<=ny<n and area[nx][ny]<area[x][y]:
            visited[nx][ny]+=1
            dfs(nx,ny)

m,n=map(int,sys.stdin.readline().split())
area=[]
for _ in range(m):
    area.append(list(map(int,sys.stdin.readline().split())))
visited=[[0]*n for _ in range(m)]
visited[0][0]=1
dfs(0,0)
print(visited[m-1][n-1])
'''