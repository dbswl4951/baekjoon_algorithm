#2xn 타일링
'''
점화식을 생각했어야 했다!
dp[i]=dp[i-1]+dp[i-2]
'''
import sys

n=int(input())
if n<=2:
    print(n)
    sys.exit(0)
dp=[0]*n
dp[0],dp[1]=1,2
for i in range(2,n):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n-1]%10007)