#도둑
import sys
from collections import deque

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n,m,k = map(int,sys.stdin.readline().split())
    arr = list(map(int,sys.stdin.readline().split()))
    result = 0
    if m==n and sum(arr)<k: result=1
    else:
        q = deque()
        right,total = 0,0
        for left in range(n):
            while len(q)<m and right<n+m-1:
                q.append(arr[right%n])
                total+=arr[right%n]
                right+=1
            if total<k: result+=1
            total -= q.popleft()
    print(result)