#친구 네트워크
'''
union find
'''
import sys
sys.setrecursionlimit(111111)

# 경로 압축 방법 사용
def find(x):
    print("find x:", x)
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def uion(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        parent[y]=x
        count[x]+=count[y]
    print(count[x])

t=int(sys.stdin.readline().strip())
for _ in range(t):
    n=int(sys.stdin.readline().strip())
    parent,count={},{}      # count: 연결 된 친구의 수

    for i in range(n):
        a,b=sys.stdin.readline().split()
        if a not in parent.keys():
            parent[a]=a
            count[a]=1
        if b not in parent.keys():
            parent[b]=b
            count[b]=1
        uion(a,b)