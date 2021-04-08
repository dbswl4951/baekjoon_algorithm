#가장 큰 정사각형
import sys

n,m=map(int,sys.stdin.readline().split())
table=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
result=0
for i in range(n):
    for j in range(m):
        # table[i][j]=0이면 (i,j)에서 정사각형을 만들 수 없다
        if i>0 and j>0 and table[i][j]==1:
            table[i][j]+=min(table[i-1][j],table[i][j-1],table[i-1][j-1])
        result=max(result,table[i][j])
print(result*result)