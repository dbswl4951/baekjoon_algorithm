#숨바꼭질
'''
한 위치에서 (-1,1,*2) 3가지로 이동 할 수 있는 옵션이 주어졌기 때문에 BFS 사용하는게 좋음!
만약 이미 방문했던 장소라면, 이전에 갔었을 때가 더 최소로 간 것이기 때문에 다시 방문하지 않음
만약 방문하지 않았고 0~100,000사이면 방문 & 기존 배열의 값에 1을 더해서 방문했다는 것을 표시

그리디 문제라고 생각해서 접근했는데 아이디어가 안떠오름
=> 힌트 보니 그래프이론(bfs)사용하는 문제였음
'''
import sys
from collections import deque

limit=100001
n,k=map(int,sys.stdin.readline().split())
find=[0]*limit
q=deque()
q.append(n)
while q:
    x=q.popleft()
    if x==k:
        break
    for i in (x-1,x+1,2*x):
        if 0<=i<limit and find[i]==0:
            find[i]=find[x]+1
            q.append(i)
print(find[k])