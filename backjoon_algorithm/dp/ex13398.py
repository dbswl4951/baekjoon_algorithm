#연속합2
'''
차원이 갈리는 DP
dp[i][0] : 수를 제거하지 않은 경우
dp[i][1] : 수를 제거 한 경우
'''
import sys

n=int(sys.stdin.readline().strip())
numbers=list(map(int,sys.stdin.readline().split()))
dp=[[0,0] for _ in range(n)]
dp[0][0]=numbers[0]
result=-int(1e9)
if n>1:
    for i in range(1,n):
        #(그 전 수를 이을건지, 현재수를 사용 할 지)
        dp[i][0]=max(dp[i-1][0]+numbers[i],numbers[i])
        #(현재 수 제거, 기존 수 제거 + 현재 수)
        dp[i][1]=max(dp[i-1][0],dp[i-1][1]+numbers[i])
        result=max(result,dp[i][0],dp[i][1])
    print(result)
else:
    print(dp[0][0])