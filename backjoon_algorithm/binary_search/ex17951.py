#흩날리는 시험지 속에서 내 평점이 느껴진거야
'''
Lower Bound

Q) 왜 답이 right일까?
    while문을 돌면서 다음 2가지 조건을 만족
    1. left <= right (최소 1이상 차이 남)
    2. group 수 : grouping(right) <= grouping(left)

    탈출 직전에 grouping(mid)>=k를 당연히 만족시키고, left = mid+1이 됨
    따라서 while문을 탈출 한 뒤,
    1. left = right +1로 역전 됨
    2. 만약 그룹 수를 체크하는 check 함수가 있다면,
     check(left) = False
     check(right) = True
'''
import sys

# 그룹 합이 score 이상 일 때 그룹 개수 count
def grouping(score):
    group,total = 0,0

    for a in arr:
        total+=a
        if total>=score:
            group+=1
            total=0
    return group <k

n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
left,right,result = 0,sum(arr)//k,0

while left<=right:
    # 그룹 최소 합 (하한선)
    mid = (left+right)//2
    if grouping(mid):
        right = mid - 1
    # 그룹 수 = k가 되는 최소 mid를 찾기 (lower bound)
    else:
        left=mid+1
print(right)
