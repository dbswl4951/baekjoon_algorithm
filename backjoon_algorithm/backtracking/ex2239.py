#스도쿠
'''
dfs + 백트레킹 문제

1. 1~10 숫자를 빈 칸에 넣어보면서 되는지 탐색
    1) 가로, 2) 세로, 3) 3x3 사각형
2-1) 된다면 dfs() 호출 => 다음 빈 칸에 넣을 숫자 탐색 (1번 부터 다시 수행)
2-2) 안된다면 다시 빈 칸 = 0으로 만들기
'''
import sys

# 빈 칸 찾기
def findZero():
    for i in range(9):
        for j in range(9):
            if board[i][j]==0: return i,j
    return None,None

# 숫자가 중복없이 채워졌는지 체크
def check(x,y,num):
    # 행 체크
    for i in range(9):
        if board[x][i]==num: return False
    # 열 체크
    for i in range(9):
        if board[i][y]==num: return False
    # 3x3 사각형 체크
    boxRow,boxCol=x//3*3,y//3*3
    for i in range(3):
        for j in range(3):
            if board[boxRow+i][boxCol+j]==num: return False
    return True

def dfs():
    x,y=findZero()
    # 빈 칸이 없으면 모두다 채워진 것
    if x==None:
        return True
    for i in range(1,10):
        # 숫자 i를 (x,y)에 넣을 수 있는지 체크
        if check(x,y,i):
            board[x][y]=i
            # 숫자 넣고 다음 탐색 시작
            if dfs(): return True
            board[x][y]=0

board=[list(map(int,sys.stdin.readline().strip())) for _ in range(9)]
dfs()
for bo in board:
    for b in bo:
        print(b,end='')
    print()