#NxM 보드 완주하기
import sys

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,count,visited,dotCnt):
    global result

    if dotCnt==0:
        result=min(result,count)
        return

    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        visit=set()
        while True:
            if nx>=n or nx<0 or ny>=m or ny<0 or board[nx][ny]=='*' or visited[nx][ny]: break
            visited[nx][ny]=1
            visit.add((nx,ny))
            dotCnt-=1
            nx, ny = nx + dx[i], ny + dy[i]
        if visit:
            dfs(nx-dx[i],ny-dy[i],count+1,visited,dotCnt)
            for vx,vy in visit:
                visited[vx][vy]=0
                dotCnt+=1

cnt=1
while True:
    temp = sys.stdin.readline().split()
    if not temp: break

    n,m = temp
    n,m =int(n), int(m)
    board=[list(sys.stdin.readline().strip()) for _ in range(n)]
    dotCnt=0
    result = 1000001
    for i in range(n):
        for j in range(m):
            if board[i][j]=='.': dotCnt+=1

    for i in range(n):
        for j in range(m):
            if board[i][j]=='.':
                visited = [[0] * m for _ in range(n)]
                visited[i][j]=1
                dfs(i,j,0,visited,dotCnt-1)

    if result==1000001:
        print('Case',cnt,end='')
        print(': -1')
    else:
        print('Case',cnt, end='')
        print(':',result)
    cnt+=1