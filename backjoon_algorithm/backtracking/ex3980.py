#선발 명단
'''
idx와 ability의 행이 같이 증가하므로, 2중 for문을 사용하지 않아도 됐다
'''
import sys

def dfs(idx,val):
    global result
    if idx==11:
        result=max(result,val)
        return
    for i in range(11):
        if ability[idx][i]==0 or select[i]:
            continue
        select[i]=1
        dfs(idx+1,val+ability[idx][i])
        select[i]=0

t=int(sys.stdin.readline().strip())
for _ in range(t):
    ability=[list(map(int,sys.stdin.readline().split())) for _ in range(11)]
    select=[0]*11
    result=0
    dfs(0,0)
    print(result)