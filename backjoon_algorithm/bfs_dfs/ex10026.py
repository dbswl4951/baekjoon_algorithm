#적록색약
'''
dfs(깊이 우선 탐색)사용
'''
import sys
#안쓰면 런타임 에러 발생!! 파이썬의 재귀 깊이 한도는 1000 정도. 이 문제에서는 dfs로 최대 10000까지 들어갈 수 있음
sys.setrecursionlimit(100000)

def dfs(x,y,pic):
    if 0<=x<n and 0<=y<n:
        if visitied[x][y]==0 and picture[x][y]==pic:
            visitied[x][y]=1
            dfs(x+1,y,pic)
            dfs(x-1,y,pic)
            dfs(x,y+1,pic)
            dfs(x,y-1,pic)
            return True
        return False
    return False

def getCount():
    count=0
    for i in range(n):
        for j in range(n):
            if dfs(i,j,picture[i][j])==True:
                count+=1
    return count

n=int(input())
picture=[list(list(input())) for _ in range(n)]
visitied=[[0]*n for _ in range(n)]

result1=getCount()  #적록색약 아닌 사람이 봤을 때의 구역 개수

for i in range(n):
    for j in range(n):
        if picture[i][j]=='G':
            picture[i][j]='R'
visitied=[[0]*n for _ in range(n)]
result2=getCount()  #적록색약인 사람이 봤을 때의 구역 개수
print(result1,result2)