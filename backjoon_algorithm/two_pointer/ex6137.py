#문자열 생성
import sys
from collections import deque

def compare(left,right):
    while left<=right:
        if arr[left]==arr[right]:
            left+=1
            right-=1
        elif arr[left]<arr[right]:
            return True
        else:
            return False
    return True

n=int(sys.stdin.readline().strip())
arr=deque([sys.stdin.readline().strip() for _ in range(n)])
result=''
while arr:
    if compare(0,len(arr)-1): result+=arr.popleft()
    else: result+=arr.pop()
for i in range(1,len(result)+1):
    print(result[i-1],end='')
    if i%80==0: print()