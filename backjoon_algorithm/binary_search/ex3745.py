#오름세
import sys
from bisect import bisect_left

while True:
    try:
        n = int(sys.stdin.readline().strip())
        arr = list(map(int,sys.stdin.readline().split()))
        result=[0]
        for a in arr:
            if result[-1]<a: result.append(a)
            else: result[bisect_left(result,a)] = a
        print(len(result)-1)
    except: break