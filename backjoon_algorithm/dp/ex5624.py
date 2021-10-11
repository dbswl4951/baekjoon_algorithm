#좋은 수
import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
one,two = {arr[0]:1},{arr[0]*2:1}
result = 0

# a+b = d-c (d는 정해진 수)
# a+b = two, c = one
for d in arr[1:]:
    for c in one:
        if d-c in two:
            result+=1
            break
    if d not in one:
        one[d]=1
    for c in one:
        if d+c not in two:
            two[d+c] = 1
print(result)