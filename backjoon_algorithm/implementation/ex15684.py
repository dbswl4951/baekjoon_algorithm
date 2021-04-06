#사다리 조작
'''
pypy 시간초과
'''
import sys

# i번째 세로선 결과가 i인지 확인
def check():
    for i in range(n):
        k=i
        for j in range(h):
            # 오른쪽으로 이동
            if board[j][k]: k+=1
            # 왼쪽으로 이동
            elif k>0 and board[j][k-1]: k-=1
        if k!=i: return False
    return True

# 사다리 놓을 수 있는 모든 경우에 사다리 놓고 check() 호출
def dfs(cnt,x,y):   # (놓은 사다리 개수, 시작 열 위치, 시작 행 위치)
    global result
    if check():
        result=min(result,cnt)
        return
    elif cnt==3 or result<=cnt:
        return

    # 행 (한 칸씩 내려감)
    for i in range(x,h):
        # k : 시작 열
        k=y if i==x else 0
        # 열 (한 칸씩 오른쪽으로)
        for j in range(k,n-1):
            if not board[i][j] and not board[i][j+1]:
                board[i][j]=1
                # y+2 : 두 가로선이 연속하지 않도록
                dfs(cnt+1,x,y+2)
                board[i][j]=0

n,m,h=map(int,sys.stdin.readline().split())
board=[[0]*n for _ in range(h)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    board[a-1][b-1]=1
result=4
dfs(0,0,0)
print(result if result<4 else -1)