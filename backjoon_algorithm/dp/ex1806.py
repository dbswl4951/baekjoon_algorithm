#부분합
'''
투포인터 문제

알고리즘 자체는 기본적이였으나, 1차 시도 : 시간초과
=> 매번 while 반복문을 돌 때마다 sum()을 구한 것이 문제
'''
import sys

n,s=map(int,sys.stdin.readline().split())
numbers=list(map(int,sys.stdin.readline().split()))
start,end=0,0
result=int(1e9)
sumVal=0
while start<=end:
    if sumVal>=s:
        result = min(result, end - start)
        sumVal -= numbers[start]
        start += 1
    elif end==n : break
    else:
        sumVal += numbers[end]
        end += 1
print(result if result!=int(1e9) else 0)