#RGB거리
import sys

n=int(sys.stdin.readline().strip())
cost=[]
for _ in range(n):
    cost.append(list(map(int,sys.stdin.readline().split())))
dp=[[0]*3 for _ in range(n)]
for i in range(n):
    if i==0:
        dp[i][0]=cost[i][0]
        dp[i][1] = cost[i][1]
        dp[i][2] = cost[i][2]
        continue
    #R
    dp[i][0]=cost[i][0]+min(dp[i-1][1],dp[i-1][2])
    #G
    dp[i][1]=cost[i][1]+min(dp[i-1][0],dp[i-1][2])
    #B
    dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])
print(min(dp[n-1]))