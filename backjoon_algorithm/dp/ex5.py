#병사 배치하기
'''
가장 긴 증가하는 부분 수열 (LIS)의 아이디어와 같음
=> 가장 긴 감소하는 부분 수열 문제로 치환
'''
import sys

n=int(sys.stdin.readline().strip())
soldier=list(map(int,sys.stdin.readline().split()))
dp=[1]*n    #1로 초기화 하는 것 중요!!!
for i in range(1,n):
    for j in range(i):  #자신의 앞에 원소 검사 (자신보다 큰 숫자가 있는지)
        if soldier[i]<soldier[j]:   #자신보다 큰 숫자가 있다면 감소하는 수열 만족하므로
            dp[i]=max(dp[i],dp[j]+1)
print(n-dp[-1])