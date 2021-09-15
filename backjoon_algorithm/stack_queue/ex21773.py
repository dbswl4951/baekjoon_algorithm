#가희와 프로세스 1
import sys,heapq

t,n = map(int,sys.stdin.readline().split())
q=[]
for _ in range(n):
    a,b,c = map(int,sys.stdin.readline().split())
    heapq.heappush(q,[-c,a,b])   # (우선순위, id, 남은시간 순)

for _ in range(t):
    prio, pId, time = heapq.heappop(q)
    # 우선순위는 상대적. 가장 우선순위가 높은 애를 뽑아서 낮추면, 모든 task의 우선순위가 올라간 것과 동일 함
    if time-1!=0:
        heapq.heappush(q,[prio+1,pId,time-1])
    print(pId)