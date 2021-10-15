#소형기관차
'''
냅색 + 누적합 문제
'''
import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
k = int(sys.stdin.readline().strip())
prefix = [0]
# 누적합 누하기
for i in range(n):
    prefix.append(prefix[-1]+arr[i])

# dp[i][j] : 기차 i대 운행 시, j번째 칸까지의 최대 승객 수
dp = [[0]*(n+1) for _ in range(4)]
for i in range(1,4):
    for j in range(i*k,n+1):
        # (그 전 객차를 이용 시 사람 수, i-1번째 객차 + 현재 j칸 이용 시 사람 수)
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-k]+prefix[j]-prefix[j-k])
print(dp[-1][-1])