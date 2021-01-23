#가장 큰 증가 부분 수열
'''
LIS 문제
'''
import sys

n=int(sys.stdin.readline().strip())
numbers=[0]+list(map(int,sys.stdin.readline().split()))
dp=[i for i in numbers]
result=0
for i in range(2,n+1):
    for j in range(1,i):
        if numbers[i]>numbers[j]:
            dp[i]=max(dp[i],numbers[i]+dp[j])
print(max(dp))