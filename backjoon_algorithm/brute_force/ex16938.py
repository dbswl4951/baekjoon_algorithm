#캠프 준비
'''
조합 사용
'''
import sys
from itertools import combinations

n,l,r,x = map(int,sys.stdin.readline().split())
levels = list(map(int,sys.stdin.readline().split()))
levelIdx = [i for i in range(n)]
result = 0

for i in range(2,n+1):
    for case in combinations(levelIdx,i):
        total,minVal,maxVal = 0,float('inf'),0
        for c in case:
            total+=levels[c]
            minVal = min(minVal,levels[c])
            maxVal = max(maxVal,levels[c])
        if l<=total<=r and maxVal-minVal>=x: result+=1
print(result)