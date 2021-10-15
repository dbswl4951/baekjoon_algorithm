import sys

n, m = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip().split() for _ in range(n)]
apple = [[0] * m for _ in range(n)]
banana = [[0] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for j in range(1, m):
    for i in range(1, n):
        if arr[i - 1][j][0] == 'B':
            banana[i][j] = banana[i - 1][j] + int(arr[i - 1][j][1:])
        else:
            banana[i][j] = banana[i - 1][j]
print('banana')
for b in banana: print(b)

for j in range(m):
    for i in range(n - 2, -1, -1):
        if arr[i + 1][j][0] == 'A':
            apple[i][j] = apple[i + 1][j] + int(arr[i + 1][j][1:])
        else:
            apple[i][j] = apple[i + 1][j]
print('apple')
for a in apple: print(a)

pf = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        pf[i][j] += banana[i][j] + apple[i][j]

for i in range(n):
    dp[i][0] = pf[i][0]

for i in range(n):
    for j in range(1, m):
        temp = int(arr[i][j][1:]) if arr[i][j][0] == 'A' else 0
        dp[i][j] = max(dp[i - 1][j] - temp, dp[i][j - 1] + pf[i][j], dp[i - 1][j - 1] + pf[i][j])

print(dp[n - 1][m - 1])