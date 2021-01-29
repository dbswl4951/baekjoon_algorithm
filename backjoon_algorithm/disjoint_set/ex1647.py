#도시 분할 계획
'''
최소 신장 트리(Minimum Spanning Tree:MST) 알고리즘 사용
1. 간선 데이터를 비용 오름차순 정렬
2. 최소 신장 트리 중 사이클이 없는 노드들의 비용을 전체 더함
3. 전체 비용 - 가장 비용이 큰 애

문제 설명 중 '유지비가 최소가 되도록 두 마을로 분리한다.'는 말은 유지비가 가장 많이 드는 길을 끊는다는 의미.
이 말 이해하기가 힘들어서 문제 설명만 참조.
'''
import sys

def findFunction(parent,x):
    if parent[x]!=x:    #부모가 자기 자신이 아니라면 부모 찾을 때 까지 재귀 함수 호출
        parent[x]=findFunction(parent,parent[x])
    return parent[x]

def unionFunction(a,b):
    a=findFunction(parent,a)
    b=findFunction(parent,b)
    if a<b: parent[b]=a
    else: parent[a]=b

def mst():
    global result,maxCost
    for i in range(1,m+1):
        cost,a,b=edges[i]
        if findFunction(parent,a)!=findFunction(parent,b):
            unionFunction(a,b)
            maxCost = max(maxCost, cost)
            result+=cost

n,m= map(int,sys.stdin.readline().split())
parent=[i for i in range(n+1)]
edges=[(0,0,0)]
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split()) #(노드a, 노드b, 비용)
    edges.append((c,a,b))
edges.sort()    #비용 오름차순 정렬
result,maxCost=0,0
mst()
print(result-maxCost)
