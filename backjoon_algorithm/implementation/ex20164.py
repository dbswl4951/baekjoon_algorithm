#홀수 홀릭 호석
import sys
from itertools import combinations

# 홀수 개수 세기
def count(n):
    cnt=0
    for i in n:
        if int(i) % 2 != 0: cnt += 1
    return cnt

def start(x,cnt):
    global minResult,maxResult

    if len(x) == 1:
        minResult = min(minResult, cnt)
        maxResult = max(maxResult, cnt)
    elif len(x) == 2:
        x = str(int(x[0]) + int(x[1]))
        cnt+=count(x)
        start(x,cnt)
    # 분할 할 수 있는 모든 케이스에 대해 3개로 나눈 후, 계속 계산 실행
    else:
        nList = list(range(1, len(x)))
        for case in combinations(nList, 2):
            first = x[:case[0]]
            second = x[case[0]:case[1]]
            third = x[case[1]:]
            temp = str(int(first) + int(second) + int(third))
            start(temp,count(temp)+cnt)

n=sys.stdin.readline().strip()
minResult,maxResult=int(1e9),0
start(n,count(n))
print(minResult,maxResult)