#피자 굽기
'''
시간 초과 때문에 다른 사람 풀이 참조. 어려웠다.
'''
import sys

d,n=map(int,sys.stdin.readline().split())
oven=list(map(int,sys.stdin.readline().split()))
pizza=list(map(int,sys.stdin.readline().split()))
for i in range(1,d):
    oven[i]=min(oven[i],oven[i-1])
depth=d-1   #아래서부터 탐색
for p in pizza:
    result=0    #맨 위에 있는 피자 깊이
    for i in range(depth,-1,-1):    #피자를 오븐에 넣자!
        if p<=oven[i]:  #피자 크기가 오븐 크기보다 작거나 같으면 넣을 수 있음
            result=i+1  #피자 깊이는 1부터 시작이므로 +1
            depth=i-1   #i에 피자를 넣었으므로 다음 피자 위치 탐색 범위는 i-1부터
            break   #피자를 넣었으니 다음 피자로 이동
    if result==0:   #피자를 하나라도 못 넣으면 실패
        break
print(result)