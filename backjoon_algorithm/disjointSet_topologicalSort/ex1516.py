#게임 개발
'''
위상 정렬 + DP
'''
import sys,copy
from collections import deque

def topologySort():
    q=deque()
    result=copy.deepcopy(time)
    for i in range(1, n + 1):
        if indgree[i] == 0: q.append(i)

    while q:
        now=q.popleft()
        for i in graph[now]:
            indgree[i]-=1
            result[i]=max(result[i],result[now]+time[i])
            if indgree[i]==0: q.append(i)
    return result

n=int(sys.stdin.readline().strip())
time=[0]
indgree=[0]*(n+1)
graph=[[] for _ in range(n+1)]
for i in range(1,n+1):
    temp=list(map(int,sys.stdin.readline().split()))
    time.append(temp[0])
    temp = temp[1:len(temp)-1]
    for t in temp:
        graph[t].append(i)
        indgree[i]+=1

result=topologySort()
for i in range(1,n+1):
    print(result[i])
