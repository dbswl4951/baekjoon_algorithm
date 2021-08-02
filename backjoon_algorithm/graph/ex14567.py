#선수 과목
'''
위상 정렬 알고리즘
'''
import sys
from collections import deque

def topologicalSort():
    q=deque()   #(연결 노드, 자기 자신 포함 선행 노드 수)
    for i in range(1,n+1):  #진입차수 0인 노드 큐에 삽입
        if indgree[i]==0:
            q.append((i,1))
    while q:
        now,t=q.popleft()
        time[now]=t
        for i in graph[now]:    #now 노드와 연결된 다른 노드들 탐색
            indgree[i]-=1   #진입차수 -1
            if indgree[i]==0:
                q.append((i,t+1))
    for i in range(1,len(time)):
        print(time[i],end=' ')

n,m=map(int,sys.stdin.readline().split())   #노드(과목)의 수,간선(조건)의 수
indgree=[0]*(n+1)   #진입차수
graph=[[] for _ in range(n+1)]  #노드에 연결된 다른 노드를 저장
time=[0]*(n+1)
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b,)
    indgree[b]+=1   #진입차수 +1
topologicalSort()