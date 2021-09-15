#도영이가 만든 맛있는 음식
import sys

def dfs(idx,bitMask,sin,sson):
    global result

    if sum(bitMask):
        result=min(result,abs(sin-sson))

    for i in range(idx,n):
        if not bitMask[i]:
            bitMask[i]=1
            dfs(i,bitMask,sin*ingredient[i][0],sson+ingredient[i][1])
            bitMask[i]=0

n=int(sys.stdin.readline().strip())
ingredient = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
bitMask =[0]*n
result = float('inf')
dfs(0,bitMask,1,0)
print(result)