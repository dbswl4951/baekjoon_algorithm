#공유기 설치
'''
집 좌표 범위가 0~10억 => 이진 탐색 사용 (O(NlogX))
1. 특정 간격(mid)을 기준으로 가능한 위치에 공유기를 설치
2. 설치한 후에는 다음과 판단
    1) 공유기 수가 더 설치되어야 한다면 (count<c), 간격을 줄인다.
    2) 공유기 수를 줄여야한다면 (count>=c), 간격을 늘린다.

다른 사람 풀이 참조하고 품
'''
import sys

n,c=map(int,sys.stdin.readline().split())
house=[]
for _ in range(n):
    house.append(int(sys.stdin.readline().strip()))
house.sort()
start=1 #최소 거리  #오답 코드!!! house[1]-house[0]
end=house[-1]-house[0]  #최대 거리
result=0

while start<=end:
    mid=(start+end)//2  #gap
    install=house[0]    #가장 최근 공유기 설치 한 위치
    count=1 #거리를 mid로 뒀을 때 공유기 설치 한 집의 개수
    for i in range(1,len(house)):
        if house[i]>=install+mid:   #공유기 설치 가능하다면
            count+=1
            install=house[i]
    if count>=c:    #공유기 수보다 공유기 설치가 많이 됐거나 같으면
        start=mid+1 #공유기 수를 줄여야 하므로, 간격을 늘림
        result=mid  #중간점의 값은 시간이 지날 수록 **최적화 된 값**이 되기 때문에,중간점의 값을 계속 기록
    else:
        end=mid-1   #공유기 수를 늘려야 하므로, 간격을 줄임
print(result)