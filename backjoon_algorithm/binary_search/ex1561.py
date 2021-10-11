#놀이 공원
'''
맨 마지막 사람이 어떤 놀이기구를 탔는지 찾기 위해선, 사람들이 언제 놀이기구를 타고 내리는지 초에 대한 정보 필요.
But, 최대 소요 시간 = Nx30(운행시간) = 60000000000이므로, 순차 탐색 시 당연히 시간초과
    => 이분 탐색을 사용해야 함

1) 이분 탐색을 통해, 사람을 모두 태울 수 있는 시간 구함 (limit 시간)
2) 마지막 탑승하는 사람은 limit 시간에 탑승할 것이므로, limit-1시간까지 탑승 한 사람이 총 몇 명인지 구함
3) limit시간에 남은 사람들을 하나씩 몇 번 놀이기구를 탔는지 확인
'''
import sys

n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
if n<m: print(n); sys.exit(0)
# 0초부터 사람들이 탑승 할 수 있으므로 left=0으로 설정
left,right,time = 0,60000000000,0

# 사람들이 모두 탑승 한 time 구함
while left<=right:
    mid = (left+right)//2
    # cnt=0으로 설정하지 않고, m으로 설정한 이유?
    # cnt는 mid시간 내에 "탄 뒤 내린 사람"이 아닌, "탑승 한" 사람의 수를 나타내기 때문
    cnt = m
    for i in range(m):
        cnt += mid//arr[i]
    if cnt>=n:
        time = mid
        right = mid-1
    else:
        left = mid+1

# 구한 시간(time)-1에 몇 명이 탈 수 있는지 구함
cnt = m
for i in range(m):
    cnt += (time-1)//arr[i]
# time초에 탑승 한 사람 구하기 (맨 마지막에 탑승 한 사람 구하기)
for i in range(m):
    # 놀이기구가 비어있다면 탑승
    if time%arr[i] == 0: cnt+=1
    if cnt == n: print(i+1); sys.exit(0)