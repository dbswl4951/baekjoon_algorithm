#상근이의 여행
'''
최소 신장 트리 알고리즘
=> 서로 다른 집합인지 확인(find) / 다르면 같은 집합으로 합치기(union)
'''
import sys

def findFuction(parent,x):
    if parent[x]!=x:
        parent[x]=findFuction(parent,parent[x])
    return parent[x]

def unionFunction(a,b):
    a=findFuction(parent,a)
    b=findFuction(parent,b)
    if a<b: parent[b]=a
    else: parent[a]=b

t=int(sys.stdin.readline().strip())
for _ in range(t):
    n,m= map(int,sys.stdin.readline().split())
    edges=[]
    for _ in range(m):
        a,b=map(int,sys.stdin.readline().split())
        edges.append((a,b))
    parent=[0]+[i for i in range(1,n+1)]
    result=0
    for edge in edges:
        a,b=edge
        if findFuction(parent,a)!=findFuction(parent,b):
            unionFunction(a,b)
            result+=1
    print(result)