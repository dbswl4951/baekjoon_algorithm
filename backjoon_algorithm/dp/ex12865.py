#평범한 배낭
'''
**Knapsack(냅샙) 알고리즘
1) 담을 수 있는 물건이 나누어 질 때(설탕 몇 g 등): 분할가능 배낭문제(Fractional Knapsack Problem)
2) 담을 수 있는 물건이 나누어 질 수 없을 때(담는다 or 안담는다): 0-1 배낭문제(0-1Knapsack Problem)
해당 문제는 0-1 배낭문제의 경우

DP로 풀었지만 실패 후 검색
DP를 1차원 배열로 만든게 실패 요인.
2차원 배열로 만들어 최적의 답 (낮은 무게, 높은 가치)를 저장!
'''
import sys

n,k=map(int,sys.stdin.readline().split())
things=[[0,0]]
for _ in range(n):
    things.append(list(map(int,sys.stdin.readline().split())))
dp=[[0]*(k+1) for _ in range(n+1)]  #가로:(무게,가치), 세로:limit무게
for i in range(1,n+1):
    for j in range(1,k+1):
        if j>=things[i][0]: #무게제한(j)가 현재 물건의 무게보다 같거나 같으면 담을 수 있음
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-things[i][0]]+things[i][1])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[n][k])