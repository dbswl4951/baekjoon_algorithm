#숨바꼭질3
'''
1. x2로 갈 수 있는 모든 점을 먼저 구한다 (appendleft())
2. x2의 점에서 -1,1로 갈 수 있는 점을 구한다

처음에 어떻게 접근해야 할지 감이 안잡혔다
'''
import sys
from collections import deque

n,k=map(int,sys.stdin.readline().split())
visited=[-1]*200001
visited[n]=0
q=deque()
q.append(n)
while True:
    x=q.popleft()
    if x==k:
        break
    if x*2<200001 and visited[x*2]==-1:
        q.appendleft(x*2)
        visited[x*2]=visited[x]
    if x-1>=0 and visited[x-1]==-1:
        q.append(x-1)
        visited[x-1]=visited[x]+1
    if x+1<200001 and visited[x+1]==-1:
        q.append(x+1)
        visited[x+1]=visited[x]+1
print(visited[k])