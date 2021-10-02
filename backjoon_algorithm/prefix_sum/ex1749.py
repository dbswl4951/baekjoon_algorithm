#점수따먹기
import sys

n,m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
result = -int(1e9)
prefix = [[0]*(m+1) for _ in range(n+1)]    # (i,j)까지의 누적 합

# 누적합 구하기
for i in range(1,n+1):
    for j in range(1,m+1):
        prefix[i][j] = prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]+board[i-1][j-1]

# (x1,y1)~(x2,y2)까지의 배열의 누적합 구한 뒤, 최댓값 갱신
for x1 in range(1,n+1):
    for y1 in range(1,m+1):
        for x2 in range(x1,n+1):
            for y2 in range(y1,m+1):
                result = max(result,prefix[x2][y2]-prefix[x2][y1-1]-prefix[x1-1][y2]+prefix[x1-1][y1-1])
print(result)