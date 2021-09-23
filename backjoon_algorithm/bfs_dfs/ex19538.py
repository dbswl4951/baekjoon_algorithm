#루머
import sys
from collections import deque

def bfs():
    while q:
        now = q.popleft()
        for next in graph[now]:
            if next==0: break
            # q에는 루머를 믿는 애들만 저장 됨
            # 즉, now는 이미 믿기 때문에 주변인 next를 돌면서 -1씩 해 줌
            remain[next] -= 1
            # 루머를 믿지 않는 사람 중, 주변인이 다 믿는 경우 => 초 구해 줌 + 큐에 삽입
            if result[next] == -1 and remain[next]==0:
                result[next] = result[now]+1
                q.append(next)

n = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n+1)]
for i in range(1,n+1):
    graph[i] = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
first = list(map(int,sys.stdin.readline().split()))
q = deque()
remain,result = [0]*(n+1),[-1]*(n+1)

# 최초 감염자 처리
for f in first:
    q.append(f)
    result[f]=0
# 루머 믿기까지 남은 사람 수 저장
for i in range(1,n+1):
    remain[i] = (len(graph[i]))//2
bfs()
for i in range(1,n+1): print(result[i],end=' ')