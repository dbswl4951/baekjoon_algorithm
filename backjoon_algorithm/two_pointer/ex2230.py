#수 고르기
import sys

n,m=map(int,sys.stdin.readline().split())
arr=[int(sys.stdin.readline().strip()) for _ in range(n)]
arr.sort(reverse=True)
left,right=0,0
result=float('inf')

while right<len(arr):
    value=arr[left]-arr[right]
    if value>=m:
        left+=1
        result=min(result,value)
        if left>right: right+=1
    else:
        right+=1
print(result)