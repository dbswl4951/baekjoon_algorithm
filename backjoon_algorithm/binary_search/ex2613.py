#숫자 구슬
import sys

# 최대 합 mid이하를 만족하는 그룹 개수 count
def countGroup(mid):
    # 마지막 그룹(mid를 넘지 않는 구슬들의 합)까지 count 해주기 위해서 group=1로 초기 설정
    group,total = 1,0

    # 구슬의 합이 최대값을 넘을 때까지 더한 후, group으로 묶음
    for a in arr:
        total+=a
        if total>mid:
            group+=1
            total=a
    return group<=m

# 구슬 채워넣고 몇 개가 들어갔는지 count
def solve(target):
    total, count,result=0,0,[]
    tm = m

    for i in range(n):
        total += arr[i]
        # 구슬을 왼쪽부터 최대한 채워넣기 위해서 상한선을 넘을 때마다 그 전까지의 값 저장
        if total>target:
            result.append(count)
            count=0
            total=arr[i]
            tm-=1
        count+=1
        if n-i == tm: break

    while tm:
        result.append(count)
        count=1
        tm-=1
    return result

n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
left,right = max(arr),sum(arr)

while left<=right:
    # 그룹 합의 최댓값 (상한선)
    mid = (left+right)//2
    if countGroup(mid):
        right = mid-1
    else:
        left = mid+1

print(left)
print(*solve(left))