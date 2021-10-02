import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]

# 일반식을 통한 prefix_sum 채우기
prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] + nums[i - 1][j - 1] - prefix_sum[i - 1][j - 1]
for p in prefix_sum: print(p)

# ans의 최솟값은 200x200칸에 모두 -10000이 들어 있는 경우인 -4억이다
# x1, y1, x2, y2를 증가시켜가며 4중 for문으로 완전탐색
# 부분행렬 구하는 것도 공식을 통해..
ans = -400000001
for x1 in range(1, N + 1):
    for y1 in range(1, M + 1):
        for x2 in range(x1, N + 1):
            for y2 in range(y1, M + 1):
                ans = max(ans,
                          prefix_sum[x2][y2] - prefix_sum[x2][y1 - 1] - prefix_sum[x1 - 1][y2] + prefix_sum[x1 - 1][
                              y1 - 1])
print(ans)