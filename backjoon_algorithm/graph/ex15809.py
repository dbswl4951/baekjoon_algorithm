#전국시대
import sys

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]

# 동맹
def union(x,y):
    x=find(x)
    y=find(y)
    if x>y:
        parent[y]=x
        people[x]+=people[y]
    else:
        parent[x]=y
        people[y]+=people[x]

# 전쟁
def war(x,y):
    x = find(x)
    y = find(y)
    if people[x] > people[y]:
        people[x] -= people[y]
        parent[y] = x
    elif people[x] < people[y]:
        people[y] -= people[x]
        parent[x] = y
    else:
        parent[x],parent[y]=0,0

n,m = map(int,sys.stdin.readline().split())
people=[0]+[int(sys.stdin.readline().strip()) for _ in range(n)]
parent=[0]+[i for i in range(1,n+1)]
for _ in range(m):
    num,x,y=map(int,sys.stdin.readline().split())
    if num==1: union(x,y)
    else: war(x,y)

result1,result2=set(),[]
for p in parent:
    p=find(p)
    if p==0: continue
    result1.add(p)
print(len(result1))
for r in result1: result2.append(people[r])
for r in sorted(result2): print(r,end=' ')