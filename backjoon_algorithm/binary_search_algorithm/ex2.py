#떡볶이 떡 만들기
'''
'현재 이 높이로 자르면 조건을 만족 할 수 있는가?' 확인 후, 조건의 만족 여부 (yes/no)에 따라 탐색 범위를 좁혀서 해결
절단기의 높이는 0~10억까지의 정수 => 이렇게 큰 탐색 범위를 보면 먼저 **이진탐색을 떠올리자

1. 입력 예시에서 가장 큰 떡의 길이가 19이므로 시작점:0, 끝점:19 => 중간점:9
2. 시작점과 끝점의 위치를 계속 바꿔가며 실행
'''
import sys

n,m=map(int,sys.stdin.readline().split())
dduck=list(map(int,sys.stdin.readline().split()))
dduck.sort()
start,end=dduck[0],dduck[-1]
h=0
while start<=end:
    mid=(start+end)//2
    sumVal=0
    for i in dduck:
        if i>mid:
            sumVal+=(i-mid)
    if sumVal>=m:
        #중간점의 값은 시간이 지날 수록 **최적화 된 값**이 되기 때문에, 떡 길이의 합이 m보다 크거나 같을 때 마다 중간점의 값을 계속 기록
        h=mid   #최대한 덜 잘랐을 때가 정답이므로, 여기에서 h에 기록
        start=mid+1
    else:
        end=mid-1
print(h)