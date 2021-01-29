#친구비
'''
1차 시도 : 분리 집합 사용 => 메모리 초과
2차 시도 : bfs
'''
import sys
from collections import deque

def bfs(i):
    global visited
    visited[i]=1
    cost=friendCost[i]
    q=deque()
    q.append(i)
    while q:
        now=q.popleft()
        for next in graph[now]:
            if visited[next]==0:
                visited[next]=1
                cost=min(cost,friendCost[next])
                q.append(next)
    return cost

n,m,k=map(int,sys.stdin.readline().split())
friendCost=[0]+list(map(int,sys.stdin.readline().split()))
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[0]*(n+1)
result=0
for i in range(1,n+1):
    if visited[i]==0:
        result+=bfs(i)
if result!=0 and result<=k: print(result)
else: print('Oh no')


#1차 시도
'''
import sys
sys.setrecursionlimit(10**8)

def findFunction(parent,x):
    if parent[x]!=x:
        parent[x]=findFunction(parent,parent[x])
    return parent[x]

def unionFunction(a,b):
    a=findFunction(parent,a)
    b=findFunction(parent,b)
    if friendCost[a]<friendCost[b]: parent[b]=a
    else: parent[a]=b

def makeFriend():
    global result
    for edge in edges:
        a,b=edge
        if findFunction(parent,a)!=findFunction(parent,b):
            unionFunction(a,b)
    cost={}
    for i in range(1,n+1):
        if parent[i] not in cost:
            cost[parent[i]]=friendCost[parent[i]]
        else:
            if friendCost[parent[i]]<cost[parent[i]]:
                cost[parent[i]]=friendCost[parent[i]]
    for r in cost.values():
        result+=r
    print(result)

n,m,k=map(int,sys.stdin.readline().split())
friendCost=[0]+list(map(int,sys.stdin.readline().split()))
edges=[]
parent=[i for i in range(n+1)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    if friendCost[a]<friendCost[b]: parent[b]=a
    else: parent[a]=b
    edges.append((a,b))
result=0
makeFriend()
'''