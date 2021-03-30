#구간 나누기2
'''
이분 탐색 응용 문제
문제 요구 사항 : 각 구간의 (최댓값-최솟값)의 최댓값 중 최솟값
mid : 각 구간의 (최댓값-최솟값)의 최댓값 중 최솟값

생각하기 어려운 문제였다..
'''
import sys

#구간 나누기 (투 포인터 사용)
def divide(mid):
    maxV=minV=numbers[0]
    cnt=1   #구간 갯수
    for i in range(1,n):
        #구간의 최대, 최소 구함
        maxV=max(maxV,numbers[i])
        minV=min(minV,numbers[i])
        #현재 구간에서 (최대-최소)가 mid(설정 한 최솟값)보다 크다면 구간 생성 가능
        if maxV-minV>mid:
            cnt+=1  #구간 생성
            #다음 구간 생성 할 수 있는지 확인 하기 위해 다음 수로 이동
            maxV=numbers[i]
            minV=numbers[i]
    return cnt

n,m=map(int,sys.stdin.readline().split())
numbers=list(map(int,sys.stdin.readline().split()))
start,end=0,max(numbers)
result=0
while start<=end:
    mid=(start+end)//2
    #구간 수가 m보다 작거나 같으면, 최솟값(mid)를 낮춰 구간 수 크게 함
    if divide(mid)<=m:
        end=mid-1
        result=mid
    else:
        start=mid+1
print(result)