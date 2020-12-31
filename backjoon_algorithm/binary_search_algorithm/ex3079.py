#입국 심사
'''
1. 심사대 오름차순으로 sort 후, 인덱스 0부터 사람 배정
2. 심사에 걸리는 시간을 기준으로 start=0,end=m*time[-1] 설정
**3. mid//t (총 심사 시간//한 개의 심사대에서 걸리는 심사 시간)이 하나의 심사대에서 검사 할 수 있는 사람
 people을 누적 시키면서 mid 시간 내에 검사 할 수 있는 총 사람의 수 구함
4. m>people이면 start=mid+1 (M보다 적은 인원을 심사하는 것은 안되므로)
 m<=people이면 end=mid-1
5. mid 출력

3번을 식으로 생각하기 어려웠다.
'''
import sys

n,m=map(int,sys.stdin.readline().split())
time=[]
for _ in range(n):
    time.append(int(sys.stdin.readline().strip()))
time.sort()
start,end=0,time[-1]*m
while start<=end:
    mid=(start+end)//2  #심사대 검사 시간의 총 합 limit
    people=0    #mid시간 동안 검사할 수 있는 총 사람의 수
    for t in time:
        # 각 심사대에서 mid 시간 동안 검사 할 수 있는 사람의 수 누적
        people+=mid//t  #이부분이 생각이 안났음
    if people<m:
        start=mid+1
    else:
        end=mid-1
print(start)