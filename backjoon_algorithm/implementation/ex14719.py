#빗물
'''
문제 해결 아이디어가 안떠올라서 다른 사람 풀이 참고
'''
import sys

h,w=map(int,sys.stdin.readline().split())
block=list(map(int,sys.stdin.readline().split()))
result=0
for i in range(len(block)):
    # 현재 인덱스의 왼쪽에서 가장 높은 건물 높이 구하기
    left=max(block[:i+1])
    # 현재 인덱스의 오른쪽에서 가장 높은 건물 높이 구하기
    right=max(block[i:])
    minBlock=min(left,right)
    # abs(현재 건물 높이 - 둘 중 더 작은 높이)
    result=result+abs(block[i]-minBlock)
print(result)