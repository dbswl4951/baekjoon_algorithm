#스도쿠
import sys

#가로 체크
def horizontal(x,val):
    if val in board[x]: return False
    return True

#세로 체크
def vertical(y,val):
    for i in range(9):
        if board[i][y]==val: return False
    return True

#3X3 체크
def square(x,y,val):
    #체크 할 시작 지점
    nx=x//3*3
    ny=y//3*3
    for i in range(3):
        for j in range(3):
            if board[nx+i][ny+j]==val: return False
    return True

def dfs(cnt):
    if cnt==len(zeros):
        for bo in board:
            for b in bo:
                print(b,end=' ')
            print()
        sys.exit(0)
    for i in range(1,10):
        nx,ny=zeros[cnt][0],zeros[cnt][1]
        if horizontal(nx,i) and vertical(ny,i) and square(nx,ny,i):
            board[nx][ny]=i
            dfs(cnt+1)
            board[nx][ny]=0

board=[list(map(int,sys.stdin.readline().split())) for _ in range(9)]
zeros=[(i,j) for i in range(9) for j in range(9) if board[i][j]==0]
dfs(0)