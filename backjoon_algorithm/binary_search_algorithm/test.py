import sys
import bisect

M, N, L= map(int, sys.stdin.readline().rstrip().split())
sandboxes=list((map(int, sys.stdin.readline().rstrip().split())))
animals=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
sandboxes.sort()
bisects=[]
count=0

for animal in animals:
    bisects.append(bisect.bisect(sandboxes, animal[0]))
print(bisects)