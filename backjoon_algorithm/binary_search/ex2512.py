#예산
'''
1. 지방 예산 요청의 합 < 국가 예산이면 요청 한 만큼 다 배정
2. 국가 예산이 모자르다면 start=0,end=max(request),mid=상한액으로 설정.
 만약 각 지방의 예산 요청이 mid보다 낮다면 sumVal에 바로 더하고, mid보다 높다면 mid값 만큼만 더함
 1) sumVal <= 국가 예산 : 상한액을 높여야 하므로 start=mid+1
 2) sumVal > 국가 예산 : 상한액을 낮춰야 하므로 end=mid-1

처음에 start=n으로 해서 틀림.
이분 탐색은 start를 뭘로 주는지가 중요 한 것 같다.
'''
import sys

n = int(input())
request=list(map(int,sys.stdin.readline().split()))
m= int(input())
request.sort()
start,end=0,request[-1]
result=0

if m>=sum(request):
    print(max(request))
    sys.exit(0)
while start<=end:
    mid=(start+end)//2  #상한액
    sumVal=0
    for i in request:
        if i>=mid:
            sumVal+=mid
        else:
            sumVal+=i
    if sumVal<=m:
        start=mid+1
    else:
        end=mid-1
print(end)