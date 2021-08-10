#진우의 민트초코 우유
import sys

def dfs(x,y,hp,cnt):
    global result
    if abs(sx-x) + abs(sy-y)<=hp: result=max(result,cnt)

    # 우유 있는 곳으로만 탐색
    for mx,my in milk:
        # 아직 안 마신 우유라면
        if board[mx][my]==2:
            dist = abs(x - mx) + abs(y - my)
            # 현재 위치에서 우유 위치까지 갈 수 있으면 가기
            if dist<=hp:
                board[mx][my]=0
                # 우유 위치로 이동
                dfs(mx,my,hp+h-dist,cnt+1)
                board[mx][my]=2

n,m,h=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
sx,sy=0,0
milk=[]
for i in range(n):
    for j in range(n):
        if board[i][j]==1: sx,sy=i,j
        elif board[i][j]==2: milk.append([i,j])
result=0
dfs(sx,sy,m,0)
print(result)