#단지 번호 붙이기
'''
dfs
'''
import sys

def dfs(x,y):
    global count
    if 0<=x<n and 0<=y<n and visited[x][y]==0 and city[x][y]==1:
        visited[x][y]=1
        count += 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

n=int(sys.stdin.readline().strip())
city=[]
for _ in range(n):
    city.append(list(map(int,sys.stdin.readline().strip())))
visited=[[0]*n for _ in range(n)]
result=[]
for i in range(n):
    for j in range(n):
        count=0
        if city[i][j]==1 and visited[i][j]==0:
            dfs(i,j)
            result.append(count)
print(len(result))
result.sort()
for r in result:
    print(r)