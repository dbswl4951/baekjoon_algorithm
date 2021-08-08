#도로 검문
import sys,heapq

def dijkstra(s,e):
    q=[]
    heapq.heappush(q,[0,1])     # (거리, 노드)
    distance = [int(1e9)] * (n + 1)
    distance[1]=0

    while q:
        dist,now = heapq.heappop(q)
        # 현재 노드가 처리 된 적 있으면 넘어가기
        if distance[now]<dist: continue
        for i in graph[now]:
            # 제외 할 경로 (s~e)면 건너뛰기
            if (s==now and e==i[0]) or (s==i[0] and e==now): continue
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,[cost,i[0]])
                # 이전 노드 저장
                if not s: route[i[0]]=now
    return distance[-1]

n,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
route=[0]*(n+1)     # 이전 노드 저장
minTime=dijkstra(0,0)   # 최소 시간
maxTime=0
e=n

# 끝 지점부터 시작점으로 가면서 검문소 만들기
while route[e]!=0:
    s=route[e]
    time=dijkstra(s,e)
    if time!=int(1e9):
        time-=minTime
        maxTime=max(maxTime,time)
    else:
        maxTime=-1
        break
    # 시작지점을 끝지점으로 설정 한 뒤, 다음 경로로 이동
    e=s
print(maxTime)