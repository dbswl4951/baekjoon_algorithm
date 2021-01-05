#1,2,3 더하기
'''
n>3일 때, dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
'''
import sys

t=int(sys.stdin.readline().strip())
result=[]
for _ in range(t):
    n=int(sys.stdin.readline().strip())
    if n<=2:
        result.append(n)
        continue
    dp=[0]*n
    dp[0],dp[1],dp[2]=1,2,4
    for i in range(3,n):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    result.append(dp[n-1])
for i in result:
    print(i)