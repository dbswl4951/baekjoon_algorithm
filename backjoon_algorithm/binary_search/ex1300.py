#k번째 수
'''
mid보다 작거나 같은 수(cnt)가 몇개인지 구한 뒤,
cnt>=k이면 start=mid-1, cnt<k이면 end=mid+1

수가 너무 커서 이분탐색으로 풀어야 겠다는 생각이 들었으나, 어떤 아이디어로 접근해야할지 너무 어려웠다
구글 풀이 본 뒤, 이해하며 풀었다
이분 탐색의 개념 뿐만 아니라, 규칙을 발견해야 풀 수 있었다
'''
import sys

n=int(sys.stdin.readline().strip())
k=int(sys.stdin.readline().strip())
start,end=1,k
result=0

while start<=end:
    mid=(start+end)//2
    cnt=0

    # 행 돌면서 mid보다 작거나 같은 수 더하기
    for i in range(1,n+1):
        # i행의 mid보다 작은 수는 mid//i 개
        cnt+=min(n,mid//i)

    if cnt>=k:
        result=mid
        end=mid-1
    else: start=mid+1

print(result)