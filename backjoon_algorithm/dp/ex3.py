#효율적인 화폐 구성
import sys

n,m=map(int,sys.stdin.readline().split())
money=[]
for _ in range(n):
    money.append(int(sys.stdin.readline().strip()))
dp=[10001]*m
dp[0]=0
for mon in money:
    for i in range(1,m):
        dp[i]=min(dp[i-mon]+1,dp[i])
if dp[m-1]==10001:
    print(-1)
else:
    print(dp[m-1])


'''
#문제집 풀이

d=[10001]*(m+1)
d[0]=0
for i in range(n):
    for j in range(money[i],m+1):
        if dp[j-money[i]]!=10001:   #(i-k)원을 만들 수 있는 경우
            dp[j]=min(dp[j],dp[j-money[i]]+1)
if dp[m-1]==10001:
    print(-1)
else:
    print(dp[m-1])
'''