#연료 채우기
import sys,heapq

n=int(sys.stdin.readline().strip())
stations=[]
for _ in range(n):
    heapq.heappush(stations,list(map(int,sys.stdin.readline().split())))
dist,fuel=map(int,sys.stdin.readline().split())
q=[]
result=0

while fuel<dist:
    # 갈 수 있는 주유소 모두 q에 넣기
    while stations and stations[0][0]<=fuel:
        d,f=heapq.heappop(stations)
        # 최대힙으로 연료 저장
        heapq.heappush(q,-f)

    # 갈 수 있는 주유소가 없으면 실패
    if not q:
        result=-1; break

    # 연료 가장 많이 채울 수 있는 곳부터 방문
    f=heapq.heappop(q)
    fuel-=f
    result+=1
print(result)