import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    if dp[x][y]: return dp[x][y]
    dp[x][y] = 1
    print("x,y=======",x,y)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if s[x][y] < s[nx][ny]:
                print("nx,ny:",nx,ny)
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
                print("dp[",x,"] [",y,"] :::",dp[x][y])
            print("dp====",dp)
    return dp[x][y]
n = int(input())
s = [list(map(int, input().split())) for i in range(n)]
dp = [[0] * n for i in range(n)]
result = 0
for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))
print(result)