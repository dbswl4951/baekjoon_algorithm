#치킨 배달
'''
브루트 포스 알고리즘!!
1. 치킨 집의 위치 중 M개를 고름 (조합)
2. 치킨 거리 계산. 최솟값을 계속 업데이트

다른 사람 풀이 참조.
'''
import sys
from itertools import combinations

n,m=map(int,sys.stdin.readline().split())
city=[]
for _ in range(n):
    city.append(list(map(int,sys.stdin.readline().split())))
house=[]
chicken=[]
for i in range(n):
    for j in range(n):
        if city[i][j]==2: chicken.append((i,j)) #치킨 집 저장
        elif city[i][j]==1: house.append((i,j)) #집 저장
result=float('inf')
for c in combinations(chicken,m):   #조합 사용. chicken에서 m개 선택
    distance=0  #치킨집에서 집까지 모든 거리 합
    for h in house: #m개의 치킨집에서 모든 집의 거리 구하기
        distance+=min([abs(h[0]-i[0])+abs(h[1]-i[1]) for i in c])
        if result<=distance: break  #그 전에 구했던 거리보다 현재 구하는 거리가 더 크면 계산 할 필요X
    if distance<result: #현재 계산 한 거리가 더 작다면 result값 갱신
        result=distance
print(result)