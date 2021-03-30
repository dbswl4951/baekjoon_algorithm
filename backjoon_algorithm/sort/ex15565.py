#귀여운 라이언
'''
투포인터 + 큐 문제
투포인터를 전에 한 번 풀었었는데 너무 오래되서 기억이 나질 않았다ㅜㅜ
'''
import sys
from collections import deque

n,k=map(int,sys.stdin.readline().split())
doll=list(map(int,sys.stdin.readline().split()))
left,right=0,0
count=0
INF=int(1e9)
result=INF
q=deque()
for i in range(n):
    while right<n and count<k:
        if doll[right]==1: count+=1
        q.append(doll[right])
        right+=1
    if count==k:
        result = min(result, len(q))
        if doll[left]==1: count-=1
        q.popleft()
        left+=1
if result==INF: print(-1)
else: print(result)