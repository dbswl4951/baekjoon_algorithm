#욕심쟁이 판다
'''
dfs 사용
시간초과 때문에 실패 후 힌트를 보고 dp를 같이 사용했다

1. dp[x][y]를 (x,y)좌표에서 가장 멀리 갈 수 있는 길이라고 할 때
dfs를 통해서 dp[x][y]가 값이 있다면 이미 예전에 (x,y)좌표에서 가장 멀리 갈 수 있는 길이를 구했다고 생각하고
다시 구할 필요없이 dp[x][y]를 리턴
2. 만약에 이전에 가지 않았다면 dp[x][y]를 1로 설정한 뒤에
상하좌우 4방향으로 dfs탐색을 통해 갈 수 있다면 1씩 값을 더 해주는 방식으로 탐색
'''
import sys
sys.setrecursionlimit(40000)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    if dp[x][y]: return dp[x][y]    #이미 값이 있다면 다시 구할 필요없이 리턴(dp)
    dp[x][y]=1  #그게 아니라면 1로 설정 후 4방향으로 dfs탐색 시작
    for i in range(4):
        nx= x+dx[i]
        ny= y+dy[i]
        if 0<=nx<n and 0<=ny<n and forest[x][y]<forest[nx][ny]:
            #재귀적으로 dfs() 호출 후, 끝까지 탐색 => 하나씩 return 하면서 dp[][]값 갱신
            dp[x][y] = max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y]

n=int(input())
forest=[]
for i in range(n):
    forest.append(list(map(int,sys.stdin.readline().split())))
dp=[[0]*n for _ in range(n)]
result=0
for i in range(n):
    for j in range(n):
        result=max(result,dfs(i,j))
print(result)