#약수의 합
import sys

t=int(sys.stdin.readline().strip())
arr=[int(sys.stdin.readline().strip()) for _ in range(t)]
dp=[0]*1000001
# 에라토스테네스의 체
for i in range(1,1000001):
    # i의 약수의 합을 더함
    for j in range(i,1000001,i):
        dp[j]+=i
    # i보다 작은 자연수의 약수 합을 더함
    dp[i]+=dp[i-1]
for a in arr: print(dp[a])