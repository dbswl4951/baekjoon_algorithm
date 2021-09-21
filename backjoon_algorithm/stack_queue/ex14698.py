#전생했더니 슬라임 연구자였던 건에 대하여 (Hard)
import sys,heapq

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr = list(map(int,sys.stdin.readline().split()))
    if len(arr)==1:
        print(1)
        continue
    q = []
    for a in arr: heapq.heappush(q,a)

    result = 1
    while len(q)>1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        result *= a*b
        heapq.heappush(q,a*b)
    print(result%1000000007)