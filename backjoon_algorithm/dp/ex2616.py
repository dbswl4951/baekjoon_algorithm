#소형 기관차
'''
DP 점화식 문제
DP[N][M] : 소형기관차를 N대 운행할 때 M번째 객차를 선택했을 경우의 최대 운송 손님 수
'''
import sys

n=int(sys.stdin.readline().strip())
train=list(map(int,sys.stdin.readline().split()))
k=int(sys.stdin.readline().strip())
sumList=[0]     #손님 누적 합
for i in range(n):
    sumList.append(sumList[-1]+train[i])
dp=[[0]*(n+1) for _ in range(4)]
for i in range(1,4):
    for j in range(i*k,n+1):
        dp[i][j]=max(dp[i][j-1],dp[i-1][j-k]+sumList[j]-sumList[j-k])
print(dp[-1][-1])