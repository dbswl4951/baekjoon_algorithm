#로봇 조립
'''
유니온 파인드 문제
'''
import sys

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    # 안쓰면 출력 초과 발생
    if a==b: return
    if a>b:
        parent[b]=a
        count[a]+=count[b]
    else:
        parent[a]=b
        count[b]+=count[a]

N=10**6+1
n=int(sys.stdin.readline().strip())
parent=list(range(N))
count=[i for i in range(N)]
for _ in range(n):
    temp=sys.stdin.readline().split()
    if temp[0]=='I':
        union(int(temp[1]),int(temp[2]))
    else:
        print(count[find(int(temp[1]))])