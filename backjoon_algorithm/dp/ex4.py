#금광
'''
dfs+dp로 풀려다가 실패

금광의 모든 위치에 대해
1. 왼쪽 위에서 오는 경우
2. 왼쪽 아래에서 오는 경우
3. 왼쪽에서 오는 경우
1,2,3 중 가장 많은 금을 가지고 있는 경우를 dp[i]애 저장
'''
import sys

t=int(sys.stdin.readline().strip())
for _ in range(t):
    n,m=map(int,sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    area=[]
    start,end=0,m
    dp=[]
    for i in range(n):
        dp.append(a[start:start+m])
        start+=m
    for j in range(1,m):
        for i in range(n):
            #왼쪽 위에서 오는 경우
            if i==0: left_up=0  #인덱스를 벗어난다면 0으로 초기화
            else: left_up=dp[i-1][j-1]
            #왼쪽 아래에서 오는 경우
            if i==n-1 : left_down=0 #인덱스를 벗어난다면 0으로 초기화
            else: left_down=dp[i+1][j-1]
            #왼쪽에서 그대로 오는 경우
            left=dp[i][j-1]
            dp[i][j]=dp[i][j]+max(left_up,left_down,left)
    result=0
    for i in range(n):
        result=max(result,dp[i][m-1])
    print(result)


'''
#<첫 시도 코드> dfs+dp
dx=[-1,0,1]
dy=[1,1,1]
def dfs(x,y):
    global visited,result
    print("x,y====",x,y)
    if y==m-1:
        result = max(result, visited[x][y])
    for i in range(3):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
            print("nx,ny::",nx,ny)
            visited[nx][ny]=visited[x][y]+area[nx][ny]
            print(visited)
            dfs(nx,ny)


t=int(sys.stdin.readline().strip())
resultList=[]
for _ in range(t):
    n,m=map(int,sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    area=[]
    start,end=0,m
    visited=[[0]*m for _ in range(n)]
    result=0
    for i in range(n):
        area.append(a[start:end])
        start,end=end,end+m
        visited[i][0] = area[i][0]
    for i in range(n):
        dfs(i,0)
    resultList.append(result)
for i in resultList:
    print(i)
'''