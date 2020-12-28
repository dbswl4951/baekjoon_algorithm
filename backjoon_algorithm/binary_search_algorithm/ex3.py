#정렬된 배열에서 특정 수의 개수 구하기
'''
시간 복잡도 O(logN)으로 알고리즘 설계하지 않으면 시간초과!

일반적인 선형 탐색으로는 시간 초과 판정 받음.
데이터가 정렬 되어 있기 때문에 이진 탐색 수행!
=>특정 값이 등장하는 첫 번째 위치와 마지막 위치를 찾아 위치 차이를 계산해 문제 해결
'''
import sys
from bisect import bisect_left,bisect_right

def countByRange(list,leftVal,rightVal):
    leftIdx=bisect_left(list,leftVal)
    rightIdx=bisect_right(list,rightVal)
    return rightIdx-leftIdx

n,x=map(int,sys.stdin.readline().split())
list=list(map(int,sys.stdin.readline().split()))

#값이 [x,x]범위에 있는 데이터 개수 계산
count=countByRange(list,x,x)
if count==0: print(-1)
else: print(count)


'''
n,x=map(int,sys.stdin.readline().split())
list=list(map(int,sys.stdin.readline().split()))
list.sort()
val=[0]*(list[-1]+1)
for i in list:
    val[i]+=1
print(val[x])
'''