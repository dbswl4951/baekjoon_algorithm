#보석 도둑
import sys, heapq

n,k=map(int,sys.stdin.readline().split())
jewelry=[]
for _ in range(n):
    heapq.heappush(jewelry,list(map(int,sys.stdin.readline().split())))
bag=[int(sys.stdin.readline().strip()) for _ in range(k)]
# 용량 제한이 작은 가방부터 먼저 담기 위해
bag.sort()
q=[]
result=0

for b in bag:
    # 1) 가방에 담을 수 있는 모든 보석의 가격을 q에 담기
    while jewelry and b>=jewelry[0][0]:
        heapq.heappush(q,-heapq.heappop(jewelry)[1])
    # 2) 훔칠 수 있는 보석 중(q), 가장 비싼 보석 훔친다
    if q: result-= heapq.heappop(q)
    # 3) 모두 다 가방에 담았으면 끝
    elif not jewelry: break
print(result)