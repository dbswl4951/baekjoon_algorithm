#공통 부분 문자열
import sys

string1 = sys.stdin.readline().strip()
string2 = sys.stdin.readline().strip()
sLen1,sLen2 = len(string1),len(string2)
dp=[[0]*(sLen2+1) for _ in range(sLen1+1)]
result=0

for i in range(1,sLen1+1):
    for j in range(1,sLen2+1):
        if string1[i-1]==string2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
            result=max(result,dp[i][j])
print(result)