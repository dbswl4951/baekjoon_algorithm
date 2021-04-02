#나머지 합
'''
O(n^2)로 구현 시 시간 초과 발생

배열 숫자들을 순서대로 더하면서 나눈 나머지를 배열 mod에 저장
나머지값이 같은 애들 중 2개를 뽑는 것 계산 => nC2 (n:나머지 값이 같은 애들 숫자)
나머지가 0인 경우, nC2 실행 시, 자기 자신도 나누어지기 때문에 mod[0]=1
'''
import sys

n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
cur=0
mod=[0]*m
mod[0]=1
for a in arr:
    # 현재의 누적합 % m
    cur=(cur+a)%m
    mod[cur]+=1
result=0
for m in mod:
    result+=m*(m-1)//2
print(result)