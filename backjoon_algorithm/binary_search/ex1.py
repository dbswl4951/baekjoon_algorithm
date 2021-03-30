#부품 찾기
'''
1. 이진 탐색 이용
2. list in 이용
3. set 이용
'''
import sys

#1. 이진 탐색 이용
'''
n=int(input())
stuck=list(map(int,sys.stdin.readline().split()))
m=int(input())
needs=list(map(int,sys.stdin.readline().split()))

def binary(stuck,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if stuck[mid]==target:
            return mid
        elif stuck[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

for target in needs:
    result=binary(stuck,target,0,n-1)
    if result!=None:
        print("yes",end=' ')
    else:
        print("no",end=' ')
'''

#3. set 사용
n=int(input())
stuck=set(map(int,sys.stdin.readline().split()))
m=int(input())
needs=list(map(int,sys.stdin.readline().split()))

for i in needs:
    if i in stuck:
        print("yes",end=' ')
    else:
        print("no",end=' ')