#두 배열의 합
import sys
from collections import defaultdict

t=int(sys.stdin.readline().strip())
n=int(sys.stdin.readline().strip())
a=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline().strip())
b=list(map(int,sys.stdin.readline().split()))

sumDic=defaultdict(int)
result=0
for i in range(n):
    for j in range(n):
        # a배열의 누적합 구하기
        if i<=j: sumDic[sum(a[i:j+1])]+=1
for i in range(m):
    for j in range(m):
        if i<=j:
            # a의 누적합 + b의 누적합 =5가 되는 개수 구하기
            result+=sumDic[t-sum(b[i:j+1])]
print(result)