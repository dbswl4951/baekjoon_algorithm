import sys
from bisect import bisect_left
input = sys.stdin.readline


while True:
    try:
        n = int(input())
        lst = list(map(int, input().split()))
        s = [0]

        for i in lst:
            print("i: ",i)
            if s[-1] < i:
                s.append(i)
            else:
                print(bisect_left(s, i))
                s[bisect_left(s, i)] = i
                print("s:",s)

        print(len(s) - 1)
    except:
        break
