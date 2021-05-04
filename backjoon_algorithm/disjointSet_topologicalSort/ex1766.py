#문제집
'''
1차 시도때 deque를 이용한 위상정렬로 풀었더니 실패
"가능하면 쉬운 문제부터 풀어야 한다." = 번호가 작은 순부터 풀어야 하므로, heapq를 이용 하면 된다
2차 시도는 heapq를 이용한 위상정렬로 풀이
'''
import sys,heapq

n,m=map(int,sys.stdin.readline().split())
indgree=[0]*(n+1)
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indgree[b]+=1

result,q=[],[]
for i in range(1,n+1):
    if indgree[i]==0: heapq.heappush(q,i)

while q:
    now=heapq.heappop(q)
    result.append(now)
    for i in graph[now]:
        indgree[i]-=1
        if indgree[i]==0: heapq.heappush(q,i)
print(*result)