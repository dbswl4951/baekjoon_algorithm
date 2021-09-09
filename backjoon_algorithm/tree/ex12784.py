#인하니카 공화국
'''
단순히 그래프 문제인줄 알았는데 트리문제였다.
"다리는 모든 섬을 연결할 수 있는 최소한의 개수로 사용되고 있다."라는 문장에서 트리 문제임을 확인 할 수 있음

리프노드들을 1번 (루트노드)와 분리를 할건데, 비용이 최소가 되도록 분리
리프 노드를 잘라도 되고, 리프노드의 부모를 잘라도 됨
즉, 리프노드 ~ 1번노드까지 봐서, 가장 비용이 적은 간선을 자르면 됨
=> 트리구조에서 1번부터 DFS 실행
'''
import sys

def dfs(cur,visited):
    visited[cur]=1
    count=0

    for i in tree[cur]:
        if not visited[i[0]]:
            # 노드가 분리되는 시점마다 비용 더하고 (dfs), 최소 비용을 더함 (+count)
            count += min(i[1],dfs(i[0],visited))
    if count==0: return float('inf')
    else: return count

t=int(sys.stdin.readline().strip())
for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
    tree=[[] for _ in range(n+1)]
    visited=[0]*(n+1)
    for _ in range(m):
        a,b,c=map(int,sys.stdin.readline().split())
        tree[a].append([b,c])
        tree[b].append([a,c])
    if n==1: print(0)
    else: print(dfs(1,visited))