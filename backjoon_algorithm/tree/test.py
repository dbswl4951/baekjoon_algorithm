import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jew = []
for _ in range(N):
    heapq.heappush(jew, list(map(int, sys.stdin.readline().split())))
bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))
bags.sort()

answer = 0
tmp_jew = []
for bag in bags:
    print("bag:",bag)
    while jew and bag >= jew[0][0]:
        print("j[0][0]:",jew[0][0])
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
        print("temp:",tmp_jew)
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
        print("answer:",answer)
    elif not jew:
        break
print(answer)