import sys
input = sys.stdin.readline

def is_possible(target):
    grpCnt = 1
    total = 0
    for number in numbers:
        total += number
        print('number, total : ',number,total)
        if total > target:
            grpCnt += 1
            total = number
            print('grpCnt:',grpCnt)

    return grpCnt <= M

def solve(target):
    count = 0
    total = 0
    result = []
    m = M
    for idx in range(N):
        total += numbers[idx]
        print('idx, total :',idx,total)
        if total > target:
            m -= 1
            total = numbers[idx]
            result.append(count)
            count = 0
            print('m, result : ',m,result)
        count += 1
        print('count:',count)
        if N - idx == m:
            break

    while m:
        result.append(count)
        count = 1
        m -= 1
        print('result, count, m : ',result,count,m)
    return result


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
left = 0
right = sum(numbers)

while left <= right:
    mid = (left + right) // 2
    print('left, right, mid : ',left,right,mid)
    if is_possible(mid):
        right = mid - 1
    else:
        left = mid + 1

print(left)
print(*solve(left))