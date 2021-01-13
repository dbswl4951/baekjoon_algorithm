#웜홀
'''
<벨만 포드 알고리즘>
다익스트라 알고리즘과 유사. But 간선 cost가 음수일 때도 사용 가능!
경로 중에 음수 사이클이 존재하는 경우를 피해 최단 거리를 계산

처음에 다익스트라 사용 => 실패 후 변경
'''
#2차 시도
import sys

def bellmanFord():
    distance = [INF] * (n + 1)  #최단 시간 저장
    for i in range(1,n+1):  #간선 개수만큼 반복 => 음수 사이클이 있는지 확인
        for j in range(1,n+1):  #각 정점마다 모든 인접 정점들을 탐색
            for now,dist in graph[j]:   #now:노드, dist:시간
                if distance[now]>dist+distance[j]:
                    distance[now]=dist+distance[j]
                    if i==n:    #음수 사이클이 존재한다면, 결과 값은 음수이므로 시간이 줄어드는 것으로 판단!
                        print("YES")
                        return
    print("NO")
    return

INF=int(1e9)
tc=int(sys.stdin.readline().strip())
for _ in range(tc):
    n,m,w=map(int,sys.stdin.readline().split()) #지점 수, 도로 수, 웜홀 수
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        x, y, z = map(int, sys.stdin.readline().split())
        graph[x].append((y, z))  #양방향
        graph[y].append((x, z))
    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().split())  #웜홀 시작 지점, 도착 지점, 줄어드는 시간
        graph[s].append((e,-t))
    bellmanFord()    #벨만포드 알고리즘 시작



#1차 시도
'''
import sys,heapq

def dijkstra(start):
    distance=[INF]*(n+1)    #최단 시간 저장
    distance[start]=0   #시작 지점은 시간 0
    q=[]
    heapq.heappush(q,(0,start)) #(시간,노드) 삽입
    while q:
        dist,now = heapq.heappop(q)
        for i in graph[now]:    #now 노드와 연결 되어 있는 모든 노드 탐색
            cost=dist+i[1]  #i[0]:노드, i[1]:시간
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance

INF=int(1e9)
tc=int(sys.stdin.readline().strip())
result=[[] for _ in range(tc)]
for test in range(tc):
    n,m,w=map(int,sys.stdin.readline().split()) #지점 수, 도로 수, 웜홀 수
    graph=[[] for _ in range(n+1)]
    wormhole=[[] for _ in range(n+1)]
    for _ in range(m):
        x,y,z=map(int,sys.stdin.readline().split())
        graph[x].append((y,z))  #양방향
        graph[y].append((x,z))
    for _ in range(w):
        s,e,t=map(int,sys.stdin.readline().split()) #웜홀 시작 지점, 도착 지점, 줄어드는 시간
        wormhole[s].append((e,t))
    distance = dijkstra(s)
    result[test] = "NO"
    for i in range(1,n+1):
        if wormhole[i]:
            list=wormhole[i]
            e,t=list.pop()
        else: continue
        if distance[e]-t<0: #시작~도착까지의 시간 - 웜홈로 줄어든 시간이 0 미만이면
            result[test]="YES"
            break
for r in result:
    print(r)
'''