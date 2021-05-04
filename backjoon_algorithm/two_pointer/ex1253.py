#졸다
import sys

n=int(sys.stdin.readline().strip())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()
result=0

# 특정 값 (arr[i]) 선택 후, 두 수의 합이 arr[i]가 되는 개수 구하기
for i in range(n):
    temp=arr[:i]+arr[i+1:]
    start,end=0,len(temp)-1
    while start<end:
        num=temp[start]+temp[end]
        if arr[i]==num:
            result+=1
            break
        elif num>arr[i]: end-=1
        else: start+=1
print(result)