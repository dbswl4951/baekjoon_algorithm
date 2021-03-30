#절댓값 힙
'''
heapq 사용
'''
import sys,heapq

n=int(sys.stdin.readline().strip())
q=[]
for _ in range(n):
    x=int(sys.stdin.readline().strip())
    if x==0:
        if q:
            a,b=heapq.heappop(q)
            print(b)
        else: print(0)
    else:
        heapq.heappush(q,(abs(x),x))