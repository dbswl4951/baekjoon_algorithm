#전시장
'''
정렬 + 이분탐색 문제

1. pictures, height를 오름차순 정렬
2. 높이가 낮은 pictures부터 시작해서 그 전까지 전시 가능 한 높이 (h-s)의 idx 구함
3. (그 전까지의 누적 합, idx 순서의 작품 누적합) 중 최대값 구함
'''
import sys
from bisect import bisect_right

n,s = map(int,sys.stdin.readline().split())
pictures, height = [],[]
for _ in range(n):
    h,c = map(int,sys.stdin.readline().split())
    pictures.append([h,c])
    height.append(h)
pictures.sort()
height.sort()
dp=[0]

for i in range(n):
    h,c = pictures[i]
    # height에서 h-s가 들어갈 위치 반환. 만약 h-s가 이미 있다면, 기존 항목 뒤의 위치 반환
    # h-s를 찾는 이유? 현재 높이(h) 전까지의 누적 가격 구하기 위해
    idx = bisect_right(height,h-s)
    # (바로 전 누적 합, h-s위치 까지의 누적합+현재 작품 가격) 중 최댓값 구함
    dp.append(max(dp[i],dp[idx]+c))
print(dp[n])