#두 용액
import sys

n=int(sys.stdin.readline().strip())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()
start,end=0,len(arr)-1
result=[]
count=float('inf')

while start<end:
    s=arr[start]+arr[end]
    if count>abs(s):
        count = abs(s)
        result=[arr[start],arr[end]]
    if s<0:
        start+=1
    else:
        end-=1
print(*result)