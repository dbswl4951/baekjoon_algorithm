#수리공 항승
'''
1. 위치의 좌우 0.5만큼 간격 줘야 함 => 길이-1 만큼 이라고 생각
2. pipe[i](i는 0~len(pipe)-1까지)과 pipe[idx] 비교 => 길이-1 만큼 차이나면 테이프 붙임

2중 while문으로 풀어도 python3로 통과 됐지만, 다른 간단한 풀이도 찾아봤다.
start = pipe[0]
end = pipe[0] + l
cnt = 1
for i in range(n):
    if start <= pipe[i] < end:
        continue
    else:
        start = pipe[i]
        end = pipe[i] + l
        cnt += 1
print(cnt)
'''
import sys

n,l = map(int,sys.stdin.readline().split())
pipe=list(map(int,sys.stdin.readline().split()))
pipe.sort()
result,i=0,0
while i<len(pipe):
    idx = i + 1
    while idx<len(pipe) and pipe[idx]-pipe[i]<=l-1:
        idx+=1
    i=idx
    result+=1
print(result)