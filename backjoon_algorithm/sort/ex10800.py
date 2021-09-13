#컬러볼
'''
1. 크기 순으로 오름차순 정렬
2. i=0번째 공부터 탐색 시작
 1) total : i전까지의(j) 모든 공 무게 합 저장
 2) color_sum : i전까지의(j) 같은 색의 무게 합 저장
 3) 현재 공 바로 전까지의(j) 총 무게 합(total) - i번째 color_sum을 구함
'''
import sys
from collections import defaultdict

n = int(sys.stdin.readline().strip())
balls=[]
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    balls.append([a,b,i])
balls.sort(key=lambda x:x[1])

result,color_sum = defaultdict(int),defaultdict(int)
total,j = 0,0
for i in range(n):
    # 현재 공보다 크기 작은 공만 잡을 수 있음
    while balls[i][1]>balls[j][1]:
        # 현재 공 전까지 모든 공 무게 합 저장
        total+=balls[j][1]
        # 색 별로 무게 저장
        color_sum[balls[j][0]]+=balls[j][1]
        j+=1
    # (잡을 수 있는 공의 총 무게 합) - (현재 공의 색과 같은 누적 무게)
    result[balls[i][2]] = total-color_sum[balls[i][0]]
for i in range(n): print(result[i])