#팰린드롬?
'''
dp[i][j] : i~j까지의 리스트가 팰린드롬인지

S~E의 길이에 따라 나눠 풀어야 함
1. 길이 1일 때 : 1
2. 길이 2일 때 : 두 문자가 같으면 1
3. 길이 3이상 일 때 : 처음 문자==끝문자 && dp[처음문자+1][끝문자-1]==1
'''
import sys

n=int(sys.stdin.readline().strip())
numbers=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline().strip())
dp=[[0]*n for _ in range(n)]

#길이 1
for i in range(n): dp[i][i]=1
# 길이 2
for i in range(n-1):
    if numbers[i]==numbers[i+1]: dp[i][i+1]=1
# 길이 3이상
for k in range(2,n):
    for i in range(n-k):
        if numbers[i]==numbers[i+k] and dp[i+1][i+k-1]==1:
            dp[i][i+k]=1
for _ in range(m):
    s,e=map(int,sys.stdin.readline().split())
    print(dp[s-1][e-1])