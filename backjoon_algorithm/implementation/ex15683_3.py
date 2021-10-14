#감시
import sys,copy

dx = [0,0,-1,1]
dy = [-1,1,0,0]
# (dx,dy)의 index 쌍으로 방향 가짐
directions = [[], [[0],[1],[2],[3]], [[0,1],[2,3]], [[1,2],[1,3],[0,3],[0,2]],
       [[0,1,2],[0,1,3],[0,2,3],[1,2,3]], [[0,1,2,3]]]

def dfs(idx,board):
    global result
    cnt=0

    if idx==len(cctvs):
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0: cnt+=1
        result = min(result,cnt)
        return

    num,x,y = cctvs[idx]
    for dir in directions[num]:
        tBoard = copy.deepcopy(board)
        for d in dir:
            nx, ny = x, y
            while True:
                nx,ny = nx+dx[d],ny+dy[d]
                if nx>=n or nx<0 or ny>=m or ny<0: break
                if tBoard[nx][ny]==6: break
                if tBoard[nx][ny]==0: tBoard[nx][ny]='#'
        dfs(idx+1,tBoard)

n,m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
cctvs = []
result = int(1e9)
for i in range(n):
    for j in range(m):
        if 0<board[i][j]<6:
            cctvs.append([board[i][j],i,j])
dfs(0,board)
print(result)