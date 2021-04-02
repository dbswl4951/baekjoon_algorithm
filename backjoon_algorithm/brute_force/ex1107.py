#리모컨
import sys

n=int(sys.stdin.readline().strip())
m=int(sys.stdin.readline().strip())
# 리모컨 조작이 가능 한 번호들
enable={str(i) for i in range(10)}
if m!=0:
    enable-=set(map(str,sys.stdin.readline().split()))
# 시작 채널인 100에서 +,-로만 움직이는 경우
minVal=abs(100-n)

# 채널이 500,000까지 이므로 +,- 모두 다 탐색해야 하므로 범위는 1000001까지
for num in range(1000001):
    # num : 리모컨 번호 버튼으로 만든 채널 번호
    num=str(num)
    for i in range(len(num)):
        # 리모컨 번호 (num[i])가 조작 가능하지 않다면
        if num[i] not in enable: break
        elif i==len(num)-1:
            # len(num)+abs(n-int(num)) : (채널 번호) + (목표 채널(n)까지 +,- 해야하는 횟수)
            minVal=min(minVal,len(num)+abs(n-int(num)))
print(minVal)