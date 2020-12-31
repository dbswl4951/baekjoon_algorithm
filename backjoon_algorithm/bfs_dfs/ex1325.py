#효율적인 해킹
'''
1. 신뢰하는 관계 => 단방향 간선으로 생각
2. 너비우선(BFS)로 탐색. 방문한 정점의 수 기록
3. 제일 많이 방문 한 시작 정점 출력

처음엔 그리디 문제라고 생각하고 그래프 완전 탐색인지 몰라서 감 못잡다가 결국 다른 사람의 풀이 봄
양방향 그래프 문제만 풀어봐서 단방향 그래프 문제에 미숙.
**단방향 관계 문제** 더 풀어 볼 것!
'''
import sys
from collections import deque

def bfs(x):
    visitied=[0]*n
    visitied[x]=1
    q=deque()
    q.append(x)
    count=1
    while q:
        x=q.popleft()
        for i in computer[x]:
            if visitied[i]==0:
                visitied[i]=1
                q.append(i)
                count+=1
    return count

n,m=map(int,sys.stdin.readline().split())
computer=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    computer[b-1].append(a-1)
result=[]
sumVal=0
for i in range(n):
        if computer[i]:
            count=bfs(i)
            if sumVal<=count:
                if sumVal<count:
                    result=[]
                sumVal=count
                result.append(i+1)
print(*result)