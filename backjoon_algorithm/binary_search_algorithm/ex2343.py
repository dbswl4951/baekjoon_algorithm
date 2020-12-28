#기타 레슨
'''
이분 탐색 => 무엇을 탐색 할 것인지가 제일 중요!
여기선 **블루레이의 최소 크기**를 찾아야 함

블루레이의 개수가 많으면 블루레이 크기를 늘리고, 블루레이 개수가 적으면 블루레이 크기를 줄여가며 이분탐색
블루레이가 45(모든 레슨들의 합)이상이면 블루레이 하나에 모든 레슨을 담을 수 있고,
블루레이가 최소 9(레슨들 중 제일 큰 값)는 되어야 블루레이에 모든 레슨을 담을 수 있음
따라서 start=9, end=45로 지정

무엇을 탐색 할 지만 빼고 ex2110과 비슷했다.
'''
import sys

n,m = map(int,sys.stdin.readline().split())
lesson=list(map(int,sys.stdin.readline().split()))
start,end=max(lesson),sum(lesson)
while start<=end:
    mid=(start+end)//2  #블루레이 길이 기준
    count=0
    sumLesson=0
    for i in lesson:
        if sumLesson+i>mid:
            count+=1
            sumLesson=0
        sumLesson+=i
    if sumLesson:   #레슨이 남아있을 경우 담아야 하므로 블루레이 count+1
        count += 1
    # 왜 count>=m는 안될까?
    # 구하는 것은 블루레이의 **최솟값**이므로, 만약 count==m이라면 mid(블루레이 길이)값을 감소 시키기 위해 end값을 줄여준다.
    if count>m:
        start=mid+1
    else:
        end=mid-1
print(start)