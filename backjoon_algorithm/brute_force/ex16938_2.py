#캠프준비
'''
dfs 사용
'''
import sys

def dfs(idx,total,minVal,maxVal):
    global result

    # 조건에 만족하더라도 return 해서 끝내면 안됨
    # 다른 수를 추가해도 또 조건에 맞을 수 있기 때문
    if l<=total<=r and maxVal-minVal>=x: result+=1
    if total>r: return

    for i in range(idx,n):
        dfs(i+1,total+levels[i],min(minVal,levels[i]),max(maxVal,levels[i]))

n,l,r,x = map(int,sys.stdin.readline().split())
levels = list(map(int,sys.stdin.readline().split()))
result = 0
dfs(0,0,float('inf'),0)
print(result)