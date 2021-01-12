#그대, 그머가 되어
'''
양방향 다익스트라
한 번에 성공!
'''
import sys
from collections import deque

def dijkstra(start):
    distance[start]=0
    q=deque()
    q.append(start)
    while q:
        now = q.popleft()
        for i in graph[now]:
            cost=distance[now]+1
            if cost<distance[i]:
                distance[i]=cost
                q.append(i)

INF=int(1e9)
a,b=map(int,sys.stdin.readline().split())   #바꾸려는 문자
n,m=map(int,sys.stdin.readline().split())   #문자수, 치환 가능 문자쌍의 수
graph=[[] for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
distance=[INF]*(n+1)
dijkstra(a)
if distance[b]==INF:print(-1)
else:print(distance[b])