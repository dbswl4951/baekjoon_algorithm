#카드 정렬하기
import sys,heapq

n=int(sys.stdin.readline().strip())
cards=[int(sys.stdin.readline().strip()) for _ in range(n)]
q=[]
for card in cards:
    heapq.heappush(q,card)
result=0
while len(q)>1:
    val1=heapq.heappop(q)
    val2=heapq.heappop(q)
    result+=val1+val2
    heapq.heappush(q,val1+val2)
print(result)