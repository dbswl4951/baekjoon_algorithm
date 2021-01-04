#개미 전사
'''
dp[i] = i번째 창고까지의 최적의 해 (얻을 수 있는 식량의 최댓값)으로 정의
 ex) storage=[1,3,1,5]
     dp=[1,3,3,8]
dp[i]를 구하기 위해서 2가지 경우를 생각 해야 함
 1) i-1번째를 털면 i번째는 못 텀
 2) i-2번째를 털면 i번째 털 수 있음
두 가지 경우 중 더 많은 식량을 얻을 수 있는 경우 선택
'''
import sys

n=int(sys.stdin.readline())
storage=list(map(int,sys.stdin.readline().split()))
dp=[0]*n
#dp 진행 (보텀업 방식)
#dp에 얻을 수 있는 식량의 최댓값을 저장
dp[0],dp[1]=storage[0],max(storage[0],storage[1])
for i in range(2,n):
    dp[i]=max(dp[i-1],dp[i-2]+storage[i])
print(dp[n-1])