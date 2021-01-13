#역사
'''
1차 시도 : 플로이드는 시간 초과 할 것이라고 생각 => 단방향 다익스트라로 구현 (실패)
2차 시도 : 힌트 본 후 플로이드 워셜 알고리즘으로 풀이 (pyhon3:시간초과, pypy3통과)
'''
#2차 시도
import sys

def floyd():
    for k in range(1,n+1):  #중간 노드
        for i in range(1,n+1):  #시작 노드
            for j in range(1,n+1):  #끝 노드
                if graph[i][j]==0:  #아직 확인하지 않은 노드라면
                    if graph[i][k]==-1 and graph[k][j]==-1:   #i->k->j일 때
                        graph[i][j]=-1   #i가 j보다 먼저 선행 됨(-1)
                    elif graph[i][k]==1 and graph[k][j]==1: #j->k->i일 때
                        graph[i][j]=1   #j가 i보다 먼저 선행 됨(1)

n,k=map(int,sys.stdin.readline().split())   #사건 개수, 전후 관계 수
graph=[[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    x,y=map(int,sys.stdin.readline().split())
    graph[x][y]=-1  #x가 먼저 일어나면 -1
    graph[y][x]=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j: graph[i][j]=0   #자기 자신으로 가는 거리는 0
s=int(sys.stdin.readline().strip()) #알고 싶은 사건 수
floyd()
for _ in range(s):
    x,y=map(int,sys.stdin.readline().split())
    print(graph[x][y])


#1차 시도
'''
import sys
from collections import deque

def dijkstra(start):
    global distance
    q=deque()
    q.append(start)
    while q:
        now = q.popleft()
        #print("now==",now)
        for i in graph[now]:    #인접 노드들 방문
            #print("i:",i)
            if distance[now][i]!=0:  #이미 들린 노드면 건너 뜀
                continue
            distance[now][i]=-1
            distance[i][now]=1
            q.append(i)
            #print("distance:", distance)

n,k=map(int,sys.stdin.readline().split())   #사건 개수, 전후 관계 수
graph=[[] for _ in range(n+1)]
for _ in range(k):
    x,y=map(int,sys.stdin.readline().split())
    graph[x].append(y)
s=int(sys.stdin.readline().strip()) #알고 싶은 사건 수
distance=[[0]*(n+1) for _ in range(n+1)]
for _ in range(s):
    x,y=map(int,sys.stdin.readline().split())
    dijkstra(x)
    print(distance[x][y])
'''