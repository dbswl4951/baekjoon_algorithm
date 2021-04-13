#공주님의 정원
'''
어떻게 풀어야 할지 감이 안잡혀서 구글 검색

1. 월,일을 비교하기 쉽게 월X100+일로 통일
2. 오름차순 정렬
3. 꽃이 피는 날=start로 고정 후, 꽃이 지는 날(date)이 가장 큰 수 저장 (=가장 늦게 지는)
4. 3번 과정에서 꽃을 한 개라도 선택 한 경우 => result+=1 + 3번 과정 다시 수행
'''
import sys

n=int(sys.stdin.readline().strip())
flowers=[]
for _ in range(n):
    m1,d1,m2,d2=map(int,sys.stdin.readline().split())
    flowers.append([m1*100+d1,m2*100+d2])
flowers.sort()

date,start,result,idx=0,301,0,-1
while start<=1130:
    flag=0
    idx+=1
    for i in range(idx,n):
        if flowers[i][0]>start: break
        if flowers[i][1]>date:
            date=flowers[i][1]
            idx=i
            flag=1
    if flag:
        result+=1
        start=date
    else:
        print(0)
        sys.exit(0)
print(result)