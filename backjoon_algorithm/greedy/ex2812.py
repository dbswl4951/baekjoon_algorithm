#크게 만들기
'''
1차 시도 : 구현 자체는 간단했는데... 시간 초과
=> 다른 사람 풀이 참조

새로 알게 된 점 : 문자열 끼리도 대소비교가 가능하다
ex) 문자열인 '3'과 '5' 대소 비교 가능
'''
import sys

n,k = map(int,sys.stdin.readline().split())
number=list(sys.stdin.readline().strip())
result,tk=[],k
for i in range(n):  #모든 문자열을 돌면서
    # 그 때마다 큰 값이 들어오면 result 값을 갱신. k번 만큼 실행.
    while tk>0 and result and result[-1]<number[i]:
        del result[-1]
        tk-=1
    result.append(number[i])
print(''.join(result[:n-k]))


#1차 시도
'''
n,k = map(int,sys.stdin.readline().split())
l=n-k
number=list(map(int,sys.stdin.readline().strip()))
result=''
startIdx,endIdx=0,k+1
while l>0:
    num=0
    for i in range(startIdx,endIdx):
        if int(num)<number[i]:
            num=str(number[i])
            startIdx=i+1
    result+=str(num)
    l-=1
    endIdx=n-l+1
    if l==len(number[startIdx:]):
        for t in number[startIdx:]:
            result+=str(t)
        break
print(result)
'''