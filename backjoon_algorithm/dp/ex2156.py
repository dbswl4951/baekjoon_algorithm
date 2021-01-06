#포도주 시식
'''
1. 이전 포도주를 먹지 않고, 현재 포도주를 먹는 경우
2. 이전 포도주를 먹고, 현재 포도주도 먹는 경우
3. 이번 포도주를 먹지 않아야 하는 경우

점화식을 생각해 내기 어려워서 다른 사람 풀이 참조 함..
출처 : https://pacific-ocean.tistory.com/152
'''
import sys

n=int(sys.stdin.readline().strip())
wine=[0]
for _ in range(n):
    wine.append(int(sys.stdin.readline().strip()))
dp=[0]
dp.append(wine[1])
if n>1:
    dp.append(wine[1]+wine[2])
for i in range(3,n+1):
    case1=dp[i-2]+wine[i]
    case2=dp[i-3]+wine[i-1]+wine[i]
    case3=dp[i-1]
    dp.append(max(case1,case2,case3))
print(dp[n])