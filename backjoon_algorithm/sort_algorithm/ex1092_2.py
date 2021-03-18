#배
import sys

m=int(sys.stdin.readline().strip())
crain=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline().strip())
box=list(map(int,sys.stdin.readline().split()))
crain.sort(reverse=True)
box.sort(reverse=True)
if crain[0]<box[0]:
    print(-1)
    sys.exit(0)
result=0
while box:
    result += 1
    for c in crain:
        for b in box:
            if c>=b:
                box.remove(b)
                break
print(result)