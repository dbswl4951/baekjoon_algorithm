#약수의 합
'''
dp[i] : i보다 작거나 같은 자연수의 모든 약수의 합

ex)
dp[4] = (1)+(1+2)+(1+3)+(1+2+4) = 15
dp[5] = (1)+(1+2)+(1+3)+(1+2+4)+(1+5) = dp[4]+(5의 약수의 합) = 21
'''
import sys

t=int(sys.stdin.readline().strip())
arr=[int(sys.stdin.readline().strip()) for _ in range(t)]
dp=[0]*1000001
# 에라토스테네스의 체
for i in range(1,1000001):
    # j의 약수의 합을 더함
    for j in range(i,1000001,i):
        dp[j]+=i
    # i전까지의 자연수의 약수 합을 더함
    dp[i]+=dp[i-1]
for a in arr: print(dp[a])