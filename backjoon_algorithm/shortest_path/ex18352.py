#특정 거리의 도시 찾기
'''
다익스트라 알고리즘

기본적인 다익스트라 문제여서 쉽고 재밌게 풀었음
'''
import sys
from collections import deque

def dijkstra(start):
    distance[start] = 0  # 시작 지점은 거리 0으로 설정
    q = deque()
    q.append(start)
    while q:
        now=q.popleft()
        for i in graph[now]:    #연결 노드 탐색
            cost=distance[now]+1
            if cost<distance[i]:    #기존 비용보다 새로 구한 경로 비용이 더 작다면 대체
                distance[i]=cost
                q.append(i) #다음 방문 경로에 저장

INF=int(1e9)
#도시개수, 도로개수, 거리, 출발 도시
n,m,k,x = map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
distance=[INF]*(n+1)
dijkstra(x) #다익스트라 알고리즘 시작
if k in distance:
    for i in range(len(distance)):
        if distance[i]==k:
            print(i)
else:
    print(-1)
