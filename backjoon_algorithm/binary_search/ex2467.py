#용액
'''
이분 탐색 사용
'''
import sys

n=int(sys.stdin.readline().strip())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()
val=float('inf')
result=[]

# 현재 값(i) 고정 후, 이분탐색으로 더할 용액(mid) 구하기
for i in range(n):
    start, end = i+1, n - 1
    while start<=end:
        mid=(start+end)//2
        temp=arr[i]+arr[mid]
        if abs(temp)<val:
            result=[arr[i],arr[mid]]
            val=abs(temp)
        if temp<0: start=mid+1
        else: end=mid-1
result.sort()
print(*result)