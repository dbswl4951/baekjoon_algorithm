#배열 돌리기 4
'''
순열 + 인덱스 사용
'''
import sys
from itertools import permutations
from copy import deepcopy

def rotate(r,c,s,arr):
    for i in range(s,0,-1): # i : 회전 하는 정사각형 (i=n:맨 바깥쪽 정사각형)
        temp=arr[r-i][c+i]
        # 맨 위
        arr[r-i][c-i+1:c+i+1]=arr[r-i][c-i:c+i]
        # 왼쪽
        for j in range(r-i,r+i):
            arr[j][c-i]=arr[j+1][c-i]
        # 아래
        arr[r+i][c-i:c+i]=arr[r+i][c-i+1:c+i+1]
        # 오른쪽
        for j in range(r+i,r-i,-1):
            arr[j][c+i]=arr[j-1][c+i]
        arr[r-i+1][c+i]=temp
    return arr

n,m,k=map(int,sys.stdin.readline().split())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
oper=[]
for _ in range(k):
    r,c,s=map(int,sys.stdin.readline().split())
    r,c=r-1,c-1
    oper.append((r,c,s))
result=int(1e9)
val=int(1e9)
for case in permutations(oper):
    temp=deepcopy(arr)
    for r,c,s in case:
        temp=rotate(r,c,s,temp)
    for t in temp:
        val=min(val,sum(t))
    result=min(result,val)
print(result)