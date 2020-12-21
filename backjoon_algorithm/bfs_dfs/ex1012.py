#유기농 배추
'''
dfs 사용
다 저장했다가 쓰는 3중 리스트 방법 쓰지 않고,
입력 받고 바로 dfs 실행 후 또 입력 받고 dfs 실행하기!
방문 한 리스트를 만들지 않고, 방문했으면 land[x][y]=-1로 변경!

문제는 간단 했는데 무한의 늪에 빠지는 실수 때문에 시간이 꽤 걸림ㅠ
'''
import sys
#안쓰면 런타임 에러 발생!! 파이썬의 재귀 깊이 한도는 1000 정도. 이 문제에서는 dfs로 최대 10000까지 들어갈 수 있음
sys.setrecursionlimit(50000)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n and land[nx][ny]==1:
            land[nx][ny]=-1
            dfs(nx,ny)

t=int(input())
result=[]
for _ in range(t):
    m,n,k=map(int,sys.stdin.readline().split())
    land = [[0] *n for _ in range(m)]
    for j in range(k):
        x,y=map(int,sys.stdin.readline().split())
        land[x][y]=1
    count=0
    for i in range(m):
        for j in range(n):
            if land[i][j]==1:
                dfs(i,j)
                count+=1
    result.append(count)
for i in result:
    print(i)