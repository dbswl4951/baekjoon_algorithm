#순회강연
import sys,heapq

n=int(sys.stdin.readline().strip())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
arr.sort(key=lambda x:x[1])
q=[]
for a in arr:
    heapq.heappush(q,a[0])
    # q에 포함된 강의의 수가 d보다 클 경우, 가장 작은 p값을 가진애 삭제
    if len(q)>a[1]:
        heapq.heappop(q)
print(sum(q))