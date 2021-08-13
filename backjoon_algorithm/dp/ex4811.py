#알약
import sys

while True:
    n=int(sys.stdin.readline().strip())
    if n==0: break

    # dp[i][j] : 알약 반 개 i번, 알약 한 개 j번 꺼냈을 때 가능한 경우의 수
    dp=[[0]*(n+1) for _ in range(n+1)]
    # 처음엔 무조건 알약 한 개를 꺼냄 => 알약 한 개 꺼내는 경우의 수 1
    for i in range(n+1):
        dp[0][i]=1
    # 한 개를 먼저 쪼개야지 반 개가 남는다
    # 따라서, 알약 반 개의 개수는 알약 한 개의 개수 보다 작다는 것이 보장 됨 (H<W)
    for i in range(1,n+1):
        for j in range(i,n+1):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    print(dp[n][n])