#다이어트
import sys,math

g=int(sys.stdin.readline().strip())
result=set()

for i in range(1,100001):
    for j in range(i,100001,i):
        num=j*j - g
        if num>0:
            if (math.sqrt(num)).is_integer():
                result.add(j)
            if math.sqrt(num)>i: break

result=list(result)
if not result: print(-1)
else:
    result.sort()
    for r in result: print(r)