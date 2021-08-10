#도서관
import sys

n,m=map(int,sys.stdin.readline().split())
minus,plus=[],[]
arr=list(map(int,sys.stdin.readline().split()))
for a in arr:
    if a>0: plus.append(a)
    else: minus.append(a)
plus.sort(reverse=True)
minus.sort()

maxVal=0
result=0
# 음수 계산
for i in range(0,len(minus),m):
    if i==0:
        maxVal=abs(minus[0])
        result+=maxVal
    else: result-=(minus[i]*2)

# 양수 계산
for i in range(0,len(plus),m):
    if i==0:
        if maxVal<plus[0]: result+=(plus[0]+maxVal)
        else: result+=(plus[0]*2)
    else: result+=(plus[i]*2)
print(result)