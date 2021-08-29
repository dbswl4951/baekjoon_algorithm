#세 수의 합
'''
[ POINT ]
세 수의 합에서 투포인터를 사용하기 위해서
두 개의 수의 합을 먼저 구하기!

1. 가장 큰 수를 찾아야 하므로 내림차순 정렬 (시간복잡도 줄이기)
2. x+y+j = i에서
 (x+y)를 묶어서 두 수의 합을 먼저 구함 => twoSum
3. twoSum = i-j가 되는 i 구함
'''
import sys

n=int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]
arr.sort(reverse=True)
twoSum = {i+j for i in arr for j in arr}
for i in arr:
    for j in arr:
        if i-j in twoSum:
            print(i)
            sys.exit(0)