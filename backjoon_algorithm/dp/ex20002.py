#사과나무
import sys

n= int(sys.stdin.readline().strip())
preSum = [[-1001]*(n+1) for _ in range(n+1)]

# (i,j)까지의 누적합 구하기
for i in range(1,n+1):
    arr=list(map(int,sys.stdin.readline().split()))
    for j in range(1,n+1):
        preSum[i][j] = preSum[i-1][j]+preSum[i][j- 1]-preSum[i-1][j-1]+arr[j-1]

result=preSum[0][0]
# 정사각형 수익만 확인
for k in range(n):
    for i in range(1,n-k+1):
        for j in range(1,n-k+1):
            result=max(result,preSum[i+k][j+k]-preSum[i-1][j+k]-preSum[i+k][j-1]+preSum[i-1][j-1])
print(result)