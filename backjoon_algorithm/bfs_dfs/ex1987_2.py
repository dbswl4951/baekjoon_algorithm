#알파벳
import sys

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,path):
    global result

    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<r and 0<=ny<c and board[nx][ny] not in path:
            path+=board[nx][ny]
            result=max(result,len(path))
            dfs(nx,ny,path)
            path=path[:len(path)-1]

r,c=map(int,sys.stdin.readline().split())
board=[list(sys.stdin.readline().strip()) for _ in range(r)]
path=board[0][0]
result=1
dfs(0,0,path)
print(result)