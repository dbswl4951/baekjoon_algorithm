#게리맨더링2
'''
브루트포스 + 구현 문제

시간이 꽤 걸렸지만 풀었다 (python3 통과)
'''
import sys
from collections import defaultdict

d=[(1,-1),(1,1),(1,1),(1,-1)]

#선거구 나누기
def divide(x,y,d1,d2):
    board = [[0] * (n+1) for _ in range(n+1)]
    board[x][y]=5
    block=defaultdict(list)
    #5선거구 경계선 구하기
    for i in range(4):
        nx,ny=x,y
        if i == 2:
            nx, ny=x+d1, y-d1
        if i == 3:
            nx, ny =x+d2, y+d2
        if 0 < nx <= n and 0 < ny <= n:
            board[nx][ny]=5
        while True:
            nx, ny = nx+d[i][0], ny+d[i][1]
            if 0<nx<=n and 0<ny<=n:
                if i==0 and (x+d1<nx or ny<y-d1): break
                if i==1 and (nx>x+d2 or ny>y+d2):break
                if i==2 and (nx>x+d1+d2 or ny>y-d1+d2):break
                if i==3 and (nx>x+d2+d1 or ny<y+d2-d1):break
                board[nx][ny]=5
                if nx in block.keys():
                    block[nx]=block[nx]+[ny]
                else:
                    block[nx]=[ny]
            else: break

    #경계선 제외 한 나머지 5선거구 채우기
    for key,value in block.items():
        if value!=None: v=set(value)
        else: continue
        if len(v)==1: continue
        value.sort()
        v1,v2=value
        for i in range(v1,v2+1):
            board[key][i]=5

    #1~4 선거구 설정
    for i in range(1,n+1):
        for j in range(1,n+1):
            if board[i][j]==0:
                if 1<=i < x + d1 and 1<=j <= y:
                    board[i][j] = 1
                elif 1<=i <= x + d2 and y< j <= n:
                    board[i][j] = 2
                elif x + d1 <= i <=n and 1<=j < y - d1 + d2:
                    board[i][j] = 3
                elif x + d2< i <=n and y - d1 + d2 <= j <= n:
                    board[i][j] = 4
    getMinimum(board)

def getMinimum(board):
    global result
    val=[0 for _ in range(5)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if board[i][j]==1:
                val[0]+=land[i][j]
            elif board[i][j]==2:
                val[1]+=land[i][j]
            elif board[i][j]==3:
                val[2]+=land[i][j]
            elif board[i][j]==4:
                val[3]+=land[i][j]
            else:
                val[4]+=land[i][j]
    result=min(result,max(val)-min(val))

n=int(sys.stdin.readline().strip())
land=[[0] * (n + 1)] +[[0]+list(map(int,sys.stdin.readline().split())) for _ in range(n)]
result=int(1e9)
for i in range(1,n+1):
    for j in range(1,n+1):
        for d1 in range(1,n+1):
            for d2 in range(1,n+1):
                if i + d1 + d2 > n:
                    continue
                if j - d1 < 1:
                    continue
                if j + d2 > n:
                    continue
                divide(i,j,d1,d2)
print(result)