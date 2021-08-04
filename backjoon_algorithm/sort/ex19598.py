#최소 회의실 개수
import sys

n=int(sys.stdin.readline().strip())
arr=[]
for _ in range(n):
    s,e= map(int,sys.stdin.readline().split())
    arr.append([s,1])
    arr.append([e,-1])
# 강의 시작 시간에 다른 강의가 끝난다면, 시작시간이 더 앞으로 오게 끔 정렬
arr.sort()

cnt,result=0,0
for a,b in arr:
    # 강의가 시작 할 때 +1, 끝날 때 -1
    cnt+=b
    # 현재 진행 중인 (시작했으나, 아직 끝나지 않은)강의의 최대 개수 구하기
    if b==1: result=max(result,cnt)
print(result)



# 1차 시도 => 실패 (시간초과)
'''
import sys,heapq

n=int(sys.stdin.readline().strip())
q=[]
for _ in range(n):
    start,end=map(int,sys.stdin.readline().split())
    heapq.heappush(q,[start,end])

result=0
while q:
    result+=1
    s,e=heapq.heappop(q)
    another=[]
    while q:
        ns,ne=heapq.heappop(q)
        if e>ns: another.append([ns,ne])
        else: e=ne

    for a in another:
        heapq.heappush(q,a)
print(result)
'''