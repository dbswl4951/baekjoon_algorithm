#해킹
'''
위상 정렬
'''
import sys
from collections import deque

def tSort():
    q=deque()
    q.append((0,c))
    distance[c]=0
    virus=set()
    virus.add(c)
    maxVal=0

    while q:
        cost,now=q.popleft()
        for i in graph[now]:
            virus.add(i[0])
            if distance[i[0]]>cost+i[1]:
                distance[i[0]]=cost+i[1]
                q.append((cost+i[1],i[0]))

    for d in distance:
        if d!=float('inf') and maxVal<d:
            maxVal=d
    print(len(virus),maxVal)

t=int(sys.stdin.readline().strip())
for _ in range(t):
    n,d,c=map(int,sys.stdin.readline().split())
    graph=[[] for _ in range(n+1)]
    distance=[float('inf')]*(n+1)
    for _ in range(d):
        a,b,s=map(int,sys.stdin.readline().split())
        graph[b].append((a,s))
    tSort()