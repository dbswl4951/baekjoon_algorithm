#구간 나누기2
'''
start : 조건을 만족하는 최댓값
end : 조건을 불만족하는 최솟값
'''
import sys

# 구간 나누기
def divideList(mid):
    count=1     # 구간 개수
    minVal,maxVal=numbers[0],numbers[0]     # 구간 시작 지점, 구간 끝 지점
    for i in range(1,n):
        minVal=min(minVal,numbers[i])
        maxVal=max(maxVal,numbers[i])
        #  (최대-최소)가 최솟값(mid) 초과면, ~i-1까지 구간 나눔
        if maxVal-minVal>mid:
            count+=1
            minVal=numbers[i]
            maxVal=numbers[i]
    return count

n,m=map(int,sys.stdin.readline().split())
numbers=list(map(int,sys.stdin.readline().split()))
start,end=0,max(numbers)
while start<=end:
    mid=(start+end)//2   # mid : (최대-최소)의 최솟값 설정
    count=divideList(mid)
    if count<=m:
        end=mid-1
    else:
        start=mid+1
print(start)