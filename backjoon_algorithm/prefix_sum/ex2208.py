#보석 줍기
import sys

n,m=map(int,sys.stdin.readline().split())
arr=[int(sys.stdin.readline().strip()) for _ in range(n)]
prefixSum=[0]
result,minSum=0,0
for i in range(n):
    prefixSum.append(prefixSum[-1]+arr[i])
for i in range(m-1,n):
    # minSum : 보석 가치를 최대로 만들기 위해 제외해야 할 가치의 합
    minSum=min(minSum,prefixSum[i - (m-1)])
    # 0~i번째 보석을 선택 후, minSum 빼기
    result=max(result,prefixSum[i+1]-minSum)
print(result)