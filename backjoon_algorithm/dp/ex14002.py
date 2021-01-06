#가장 긴 증가하는 부분 수열4
'''
DP를 사용한 LIS
=> O(N^2)

가장 긴 증가하는 부분 수열의 길이는 구했으나 가장 긴 증가하는 부분 수열 출력 하는 것을 못해서 풀이 참조
'''
import sys

n=int(sys.stdin.readline().strip())
numbers=list(map(int,sys.stdin.readline().split()))
dp=[1]*n
#수열의 길이 구하기
for i in range(1,n):
    for j in range(i):
        if numbers[i]>numbers[j]:
            dp[i]=max(dp[j]+1,dp[i])

result=[]
dpVal=max(dp)
dpIdx=dp.index(dpVal)
#수열 구하기
while dpIdx>=0: #가장 큰 숫자의 인덱스부터 내려가면서 검사사
    if dp[dpIdx]==dpVal:
        result.append(numbers[dpIdx])
        dpVal-=1
    dpIdx-=1
print(max(dp))
for i in result[::-1]:
    print(i,end=' ')