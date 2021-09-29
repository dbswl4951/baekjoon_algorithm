#회전 초밥
import sys
from collections import defaultdict

n,d,k,c = map(int,sys.stdin.readline().split())
sushi = [int(sys.stdin.readline().strip()) for _ in range(n)]
sushi.extend(sushi)
# 먹은 초밥 번호 counting
sushiDict = defaultdict(int)
sushiDict[c] = 1
left,result = 0,0

for right in range(n+k-1):
    sushiDict[sushi[right]] += 1

    # 초밥을 총 k개 이상 먹었으면 조건에 만족
    if right>=k-1:
        result = max(result,len(sushiDict))
        sushiDict[sushi[left]] -= 1
        if sushiDict[sushi[left]]==0:
            del sushiDict[sushi[left]]
        left += 1
print(result)