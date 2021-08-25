#내일 할거야
import sys

n = int(sys.stdin.readline().strip())
arr=[]
for _ in range(n):
    a,b=map(int,sys.stdin.readline().split())
    arr.append([b,a])
arr.sort(reverse=True)
day=arr[0][0]
for limit,time in arr:
    if day>limit: day=limit-time
    else: day-=time
print(day)