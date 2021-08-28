#화장실의 규칙
import sys, heapq
from collections import deque

n,m,k = map(int,sys.stdin.readline().split())
waiting,q=[deque() for _ in range(m)],[]
for i in range(n):
    d,h = map(int,sys.stdin.readline().split())
    if i==k: waiting[i%m].append([-d,-h,i%m,1])
    else: waiting[i%m].append([-d,-h,i%m,0])
# 초기 선두주자들 q에 넣기
for i in range(m):
    if waiting[i]:
        d,h,idx,flag = waiting[i].popleft()
        heapq.heappush(q,[d,h,idx,flag])

result=0
while True:
    d,h,idx,flag = heapq.heappop(q)
    # 데카면 stop
    if flag: break

    result+=1
    # 새 선두주자 q에 넣기
    if waiting[idx]:
        heapq.heappush(q,waiting[idx].popleft())
print(result)