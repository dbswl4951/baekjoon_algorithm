#Count Circle Groups
'''
union-find가 끝난 후, 그룹 개수 구할 때 len(set(parent))로 구했더니 시간초과 났다.
result라는 상수 변수를 두고, 그룹 합칠 때마다 -1 해줘서 그룹 개수를 구해야 시간초과가 나지 않는다.
'''
import sys

# 두 진영 사이의 거리 구하기
def getDistance(x,y,d,nx,ny,nd):
    dist=(x-nx)**2+(y-ny)**2
    if dist<=(d+nd)**2: return 1
    return 0

def union(parent,x,y):
    x=find(parent,x)
    y=find(parent,y)
    if x>y: parent[x]=y
    else: parent[y]=x

def find(parent,x):
    if parent[x]!=x:
        parent[x]=find(parent,parent[x])
    return parent[x]

t=int(sys.stdin.readline().strip())
for _ in range(t):
    n=int(sys.stdin.readline().strip())
    nodes=[]
    parent=[i for i in range(n)]
    for i in range(n):
        a,b,c=map(int,sys.stdin.readline().split())
        nodes.append([i,a,b,c])

    result=n
    for i in range(n):
        for j in range(i+1,n):
            num,x,y,d=nodes[i]
            nnum,nx,ny,nd=nodes[j]
            # 두 진영이 통신 할 수 있고, 그룹이 같지 않다면 합치기
            if getDistance(x,y,d,nx,ny,nd) and find(parent,num)!=find(parent,nnum):
                union(parent,num,nnum)
                result-=1
    print(result)