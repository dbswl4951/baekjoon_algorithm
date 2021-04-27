#암호 만들기
import sys
from itertools import combinations

con=['a','e','i','o','u']
l,c=map(int,sys.stdin.readline().split())
alpha=list(sys.stdin.readline().split())
result=[]
for case in combinations(alpha,l):
    case = list(case)
    cnt=0
    for c in case:
        if c in con: cnt+=1
    if cnt and len(case)-cnt>=2:
        case.sort()
        result.append(case)
result.sort()
for res in result:
    for r in res:
        print(r,end='')
    print()