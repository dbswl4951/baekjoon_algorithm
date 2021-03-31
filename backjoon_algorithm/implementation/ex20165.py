#인내의 도미노 장인 호석
import sys,copy
from collections import deque

dx=[0,0,-1,1]
dy=[1,-1,0,0]

# 도미노 공격
def hit(x,y,d):
    global result
    if x<0 or x>=n or y<0 or y>=m: return
    k=board[x][y]
    for i in range(1,k):
        nx,ny=x+i*dx[d],y+i*dy[d]
        hit(nx,ny,d)
    # 도미노 쓰러뜨리기
    if board[x][y]!=0:
        result+=1
        board[x][y]=0

# 도미노 방어
def up(x,y):
    if x<0 or x>=n or y<0 or y>=m: return
    board[x][y]=copyBoard[x][y]

n,m,r=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# 도미노를 다시 세울 때, 원래 도미노의 높이 구하기 위해서
copyBoard=copy.deepcopy(board)
attact,defence=deque(),deque()
for _ in range(r):
    a,b,c=sys.stdin.readline().split()
    d,e=map(int,sys.stdin.readline().split())
    if c=='E': c=0
    elif c=='W': c=1
    elif c=='N': c=2
    else: c=3
    attact.append([int(a)-1,int(b)-1,c])
    defence.append([d-1,e-1])
    
result=0
for i in range(r):
    hit(*attact[i])
    up(*defence[i])
for i in range(n):
    board[i]=['S' if j!=0 else 'F' for j in board[i]]
print(result)
for i in range(n):
    print(*board[i])