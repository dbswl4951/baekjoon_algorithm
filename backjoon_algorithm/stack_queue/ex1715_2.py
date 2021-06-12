#카드 정렬하기
import sys,heapq

n=int(sys.stdin.readline().strip())
q=[]
result=0
for _ in range(n):
    heapq.heappush(q,int(sys.stdin.readline().strip()))
while len(q)>1:
    a=heapq.heappop(q)
    b=0
    if q: b=heapq.heappop(q)
    result+=(a+b)
    heapq.heappush(q,a+b)
print(result)