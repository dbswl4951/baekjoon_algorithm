#LCS
'''
비교하는 위치의 문자가 서로 같으면 현재 위치의 값 = 왼쪽 대각선 값 + 1  (배열 범위를 벗어났으면 0이라고 가정 )
다르다면 현재 위치의 값 = MAX{왼쪽 값, 위쪽 값}

40분 동안 고민 했지만 풀지 못해서 검색
'''
import sys

str1=list(sys.stdin.readline().strip())
str2=list(sys.stdin.readline().strip())
len1,len2=len(str1),len(str2)
dp=[[0]*(len2+1) for _ in range(len1+1)]
for i in range(len1):
    for j in range(len2):
        if str1[i]==str2[j]:
            dp[i+1][j+1]=dp[i][j]+1 #왼쪽 대각선 값+1
        else:
            dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j]) #왼쪽,위쪽 값 중 큰 값
print(dp[len1][len2])