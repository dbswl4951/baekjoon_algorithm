'''
우선 순위 큐로 풀기 시도 => 실패
풀이 찾아보니 dp 배낭 알고리즘으로 풀어야 했다
'''
#앱
import sys

n,m=map(int,sys.stdin.readline().split())
memory=[0]+list(map(int,sys.stdin.readline().split()))
costs=[0]+list(map(int,sys.stdin.readline().split()))
# dp[i][j] : i번째 앱과 j비용으로 확보 가능 한 메모리
dp=[[0]*(sum(costs)+1) for _ in range(n+1)]
result=float('inf')

for i in range(1,n+1):  # 앱 번호
    for j in range(1,sum(costs)+1):  # cost
        # 현재 cost로 앱을 비활성 시킬 수 없는 경우
        if j<costs[i]: dp[i][j]=dp[i-1][j]
        # max(그 전까지의 메모리 확보 양 (dp[i-1][j]),
        #   현재 앱(i)만큼의 cost를 확보한 뒤 (dp[i-1][j-costs[i]]), 현재 앱을 비활성 시켜(+memory[i]) 얻는 메모리 확보 양)
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-costs[i]]+memory[i])
        if dp[i][j]>=m: result=min(result,j)
print(result)