#자동차경주
'''
2가지 풀이 가능 (다익스트라, 위상정렬)
위상정렬로 풀이
'''
import sys
from collections import deque

def topological():
    q=deque()
    q.append(1)
    # 사이클 없애기 위해 시작 지점(1) 진입 차수를 0으로 설정
    indegree[1]=0

    while q:
        now = q.popleft()
        for i in graph[now]:
            cost = distance[now]+i[1]
            indegree[i[0]]-=1
            if cost>distance[i[0]]:
                distance[i[0]]=cost
                prev[i[0]]=now
            if indegree[i[0]]==0:
                q.append(i[0])

n=int(sys.stdin.readline().strip())
m=int(sys.stdin.readline().strip())
graph=[[] for _ in range(m+1)]
indegree,distance,prev = [0]*(n+1),[0]*(n+1),[0]*(n+1)
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
    indegree[b]+=1
topological()
print(distance[1])
temp,idx=[1],1
while True:
    node = prev[idx]
    temp.append(node)
    if node==1: break
    idx=node
for i in range(len(temp)-1,-1,-1): print(temp[i], end=' ')