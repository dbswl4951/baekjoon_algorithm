#안정된 집단
import sys

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x>y:
        parent[x]=y
    else:
        parent[y]=x

n = int(sys.stdin.readline().strip())
parent = [i for i in range(n+1)]
for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    for j in range(n):
        if temp[j]==0 and i!=j:
            if find(i+1)!=find(j+1):
                union(i+1,j+1)
#print(parent)
result = [[] for _ in range(n+1)]
count = 0
for i,p in enumerate(parent):
    result[p].append(i)
for i in range(1,n+1):
    if len(result[i])>1: count+=1
if count ==0:
    print(0)
else:
    print(count)
    for i in range(1,n+1):
        if len(result[i])>1:
            print(*result[i])