#크리보드
'''
- N = 1~6까지는 복붙을 하지 않고 1번만 수행하는게 이득
- N = 7부터는 복붙을 이용하는게 이득
    선택, 복사, 붙여넣기 -> 3번 액션 필요
    따라서 N=8이라면, j = 5부터 시작해서 1번 복붙 할 때 (5+3=8번 액션)
    j = 5일 때 1 5번 수행 + 복붙 1번
    j = 4일 때 1 4번 수행 + 복붙 2번
'''
import sys

n = int(sys.stdin.readline().strip())
dp=[i for i in range(n+1)]
for i in range(7,n+1):
    # 최소 i-3번째 시작해야 복붙을 수행 할 수 있다
    for j in range(i-3,-1,-1):
        dp[i] = max(dp[i],dp[j]*(i-j-1))
print(dp[n])