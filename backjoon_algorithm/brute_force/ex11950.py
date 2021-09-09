#2016 IOI
import sys

def dfs(i,j,preSum):
    global result

    # 첫번째 줄 => 무조건 흰색
    if i==0: dfs(i+1,j,preSum+count[i][0])
    # 마지막 줄 => 무조건 빨간색
    elif i==n-1:
        if j==0: return
        # 빨간색 줄로 만든 후, count
        tmp = preSum+count[i][2]
        result=min(result,tmp)
    # 중간 줄
    else:
        # 현재 색 유지하면서 아래 줄로 이동
        dfs(i+1,j,preSum+count[i][j])
        # 다음 색으로 변경
        if j!=2: dfs(i+1,j+1,preSum+count[i][j+1])

n,m = map(int,sys.stdin.readline().split())
count = [[m]*3 for _ in range(n)]
for i in range(n):
    temp = list(sys.stdin.readline().strip())
    for j in range(m):
        if temp[j]=='W': count[i][0]-=1
        elif temp[j]=='B': count[i][1]-=1
        else: count[i][2]-=1
result=int(1e9)
dfs(0,0,0)
print(result)