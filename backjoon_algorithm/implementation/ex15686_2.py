#치킨 배달
import sys
from itertools import combinations

# 집~치킨집 사이의 거리 구하기
def getDistance(x,y,case):
    dist=int(1e9)
    for c in case:
        dist=min(dist,abs(x-c[0])+abs(y-c[1]))
    return dist

n,m=map(int,sys.stdin.readline().split())
board=[]
chicken=[]
for i in range(n):
    temp=list(map(int,sys.stdin.readline().split()))
    board.append(temp)
    for j in range(n):
        if temp[j]==2:
            chicken.append([i,j])
result=int(1e9)
for case in combinations(chicken,m):
    count=0
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                count+=getDistance(i,j,case)
    result=min(result,count)
print(result)