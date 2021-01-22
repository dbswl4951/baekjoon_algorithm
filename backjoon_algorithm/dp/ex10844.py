#쉬운 계단 수
import sys

n=int(sys.stdin.readline().strip())
dp=[[1]*10 for _ in range(n+1)]
dp[1][0]=0  #길이 1인 수는 0으로 시작 할 수 없음
for i in range(2,n+1):  #수의 자리 : 2~n
    for j in range(0,10):   #수는 0~9로 만들 수 있다
        if j==0:
            dp[i][j]=dp[i-1][j+1]   #그 전 수 자리에서 1로 만들 수 있는 수의 개수
        elif j==9:  #그 전 수 자리에서 8로 만들 수 있는 수의 개수
            dp[i][j]=dp[i-1][j-1]
        else:
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]
print(sum(dp[n])%1000000000)