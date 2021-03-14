#LCS 3
'''
문자열 내의 모든 문자를 방문하며 비교해야 함
=> O(N^3)

LIS 문제는 풀어봤는데, LCS 문제는 처음 풀어봤다.
여러가지 유형 익히는 것이 중요!!
'''
import sys

s1,s2,s3=[sys.stdin.readline().strip() for _ in range(3)]
dp=[[[0]*(len(s3)+1) for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        for k in range(1,len(s3)+1):
            #같은 문자가 나오면 이전까지 LCS길이 (대각선 왼쪽 위) +1
            if s1[i-1]==s2[j-1]==s3[k-1]:
                dp[i][j][k]=dp[i-1][j-1][k-1]+1
            #다른 문자라면, 직전 LCS 값 중 제일 큰 값
            else:
                dp[i][j][k]=max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])
result=0
for i in dp:
    for j in i:
        result=max(result,max(j))
print(result)