#우유 도시
'''
구현+dfs 문제인줄 알았으나, dp문제였다
'''
import sys

n=int(sys.stdin.readline().strip())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]    # 최대로 먹을 수 있는 우유 수 저장
now=0   # 먹어야 할 우유 번호

for i in range(n):
    for j in range(n):
        # 첫 시작점 검사
        if i==0 and j==0:
            if board[i][j]==now: dp[i][j]=1
        # 맨 윗 줄은 오른쪽 이동만 가능
        elif i==0:
            cnt=dp[i][j-1]
            now=cnt%3
            if board[i][j]==now: dp[i][j]=cnt+1
            else: dp[i][j]=cnt
        # 맨 오른쪽 줄은 아래로 이동만 가능
        elif j==0:
            cnt=dp[i-1][j]
            now=cnt%3
            if board[i][j]==now: dp[i][j]=cnt+1
            else: dp[i][j]=cnt
        else:
            # 그 외의 좌표는 왼쪽, 위쪽에서 올 수 있음
            cnt=max(dp[i-1][j],dp[i][j-1])
            now=cnt%3
            if board[i][j]==now: dp[i][j]=cnt+1
            else: dp[i][j]=cnt
print(dp[n-1][n-1])