#빵집
import sys

dx = [-1,0,1]
dy = [1,1,1]

def dfs(x,y):
    global result, flag

    if flag: return
    if y == c-1:
        result+=1
        flag = 1
        return

    for i in range(3):
        nx,ny = x+dx[i],y+dy[i]
        if flag: return
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != 'x':
            board[nx][ny] = 'x'
            dfs(nx,ny)

r,c = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(r)]
result = 0
for i in range(r):
    flag = 0
    dfs(i,0)
print(result)