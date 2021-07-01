#휴게소 세우기
import sys

def countBuilding(mid):
    # 세운 휴게소 개수
    count=0
    for i in range(1,len(location)):
        if location[i]-location[i-1]>mid:
            # -1을 해주는 이유는 이미 휴게소가 있는 곳에 또 세우는 것을 막기 위함
            count +=(location[i]-location[i-1]-1)//mid
    return count

n,m,l=map(int,sys.stdin.readline().split())
location=list(map(int,sys.stdin.readline().split()))
location.append(0)
location.append(l-1)
location.sort()

start,end=0,l-1
result=0
while start<=end:
    mid=(start+end)//2
    count=countBuilding(mid)
    if count>m:
        start=mid+1
    else:
        # 만약 count<=m이면 최댓값의 최솟값인 mid를 저장 후,
        # mid보다 더 최솟값을 찾기 위해 end를 줄여줌
        result = mid
        end=mid-1
print(result)