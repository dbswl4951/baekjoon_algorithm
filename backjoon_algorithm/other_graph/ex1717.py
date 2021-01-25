#집합의 표현
'''
Union Find (Disjoint Set) 알고리즘
'''
import sys
sys.setrecursionlimit(100000)

def unionFunction(parent,x,y):
    x=findFuction(x)
    y=findFuction(y)
    #더 큰 값을 가진 값의 부모를 작은 값으로 설정
    if x<y: parent[y]=x
    else: parent[x]=y

#경로 압축 방법 사용
def findFuction(x):
    #루트 노드를 찾을 때 까지 재귀 호출
    if parent[x]!=x:
        parent[x]=findFuction(parent[x])
    return parent[x]

n,m=map(int,sys.stdin.readline().split())
uf=[]
parent=[i for i in range(n+1)]    #부모를 자기 자신으로 초기화
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    uf.append([a,b,c])
for u in uf:
    a,b,c=u
    if a==0: #union
        unionFunction(parent,b,c)
    else:   #find
        if findFuction(b)==findFuction(c):
            print('YES')
        else: print('NO')