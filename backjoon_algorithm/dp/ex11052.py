#카드 구매하기
'''
dp[i] = 카드 i개 구매하는 최대 가격,
p[k] = k개가 들어있는 카드팩 가격 이라고 했을때 카드를 i개 구매하는 최대 비용
d[1] = d[0] + p[1]
d[2] = d[1] + p[1] or d[0] + p[2]
d[3] = d[2] + p[1] or d[1] + p[2] or d[0] + p[3]
d[4] = d[3] + p[1] or d[2] + p[2] or d[1] + p[3] or d[0] + p[4]

처음에 어떻게 할지 감 못잡다가 힌트 봄
=> 작은 문제부터 생각!! 점화식 도출 하는 문제
'''
import sys

n=int(sys.stdin.readline().strip())
price=[0]+list(map(int,sys.stdin.readline().split()))
dp=[0]*(n+1)
dp[1]=price[1]  #카드 1개 구매 할 때 가격은 price[1]
for i in range(2,n+1):
    for j in range(1,i+1):
        dp[i]=max(dp[i],dp[i-j]+price[j])
print(dp[n])