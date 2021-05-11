#수 묶기
import sys

n=int(sys.stdin.readline().strip())
minus,plus=[],[]
for _ in range(n):
    x=int(sys.stdin.readline().strip())
    if x<=0: minus.append(x)
    else: plus.append(x)
minus.sort()
plus.sort(reverse=True)

result=[]
mIdx,pIdx=0,0
while mIdx<len(minus):
    if mIdx<len(minus)-1:
        result.append(minus[mIdx]*minus[mIdx+1])
        mIdx+=2
    else:
        result.append(minus[mIdx])
        mIdx+=1
while pIdx<len(plus):
    if pIdx<len(plus)-1 and plus[pIdx]!=1 and plus[pIdx+1]!=1:
        result.append(plus[pIdx]*plus[pIdx+1])
        pIdx+=2
    else:
        result.append(plus[pIdx])
        pIdx+=1
print(sum(result))