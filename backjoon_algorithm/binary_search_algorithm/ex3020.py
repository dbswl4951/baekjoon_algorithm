#개똥벌레
'''
<3차 시도> => 이분 탐색 이용
1. 석순,종유석을 따로 list에 담고 오름차순으로 sort
2. start=0,end=len(cave)-1로 지정 후 (탐색 대상은 장애물), 중간 인덱스인 cave[mid]검사
 => x이상의 장애물이 몇 개 있는지
 1) 만약 cave[mid]가 지정 높이(x)보다 작거나 같다면 탐색범위를 start=mid+1부터 시작
 2) cave[mid]가 지정 높이(x)보다 크다면 탐색 범위를 end=mid-1까지로 지정
'''
import sys

def binary_search(cave,x):  #주어진 list에서 x보다 큰 데이터의 개수를 반환
    right,left=0,len(cave)-1
    while right<=left:
        mid=(right+left)//2
        if cave[mid]<=x:
            right=mid+1
        else:
            left=mid-1
    # x이하의 값을 갖는 데이터 중 최댓값의 index: right
    # x이하의 값을 갖는 데이터의 개수: right + 1 (index는 0부터 시작하므로)
    # x보다 큰 데이터의 개수: 전체 데이터의 개수 - (right + 1)
    return len(cave)-(right+1)

n,h=map(int,sys.stdin.readline().split())
cave1=[]    #석순 list
cave2=[]    #종유석 list
for i in range(n):
    if i%2==0:
        cave1.append((int(sys.stdin.readline().strip())))
    else:
        cave2.append((int(sys.stdin.readline().strip())))
cave1.sort()
cave2.sort()
result1=n   #장애물의 최솟값
result2=0   #구간 몇 개 있는지
for i in range(1,h+1):
    cave1Num=binary_search(cave1,i-1)
    cave2Num=binary_search(cave2,h-i)
    sumNum=cave1Num+cave2Num
    if sumNum<result1:
        result1=sumNum
        result2=1
    elif sumNum==result1:
        result2+=1
print(result1,result2)


'''
<2차 시도>
1. 석순,종유석을 따로 list에 담음
2. h마다 검사 후 가장 최솟값을 저장
2차원 list때문에 메모리 초과 나는 것으로 생각하여 석순,종유석을 따로 1차원 list에 담아서 코딩.
이때까지만해도 이게 왜 꼭 이분탐색으로 풀어야 하는지 잘 몰랐음
=>시간 초과
'''
'''
import sys

n,h=map(int,sys.stdin.readline().split())
cave1=[]    #석순 list
cave2=[]    #종유석 list
for i in range(n):
    if i%2==0:
        cave1.append(int(input()))
    else:
        cave2.append(int(input()))
result1=float('inf')
result2=1
for i in range(1,h+1):
    count=0
    for j in range(len(cave1)):
        if cave1[j]>=i:
            count+=1
        if h-i+1<=cave2[j]:
            count+=1
        print("count:",count)
    if result1 == count:
        result2 += 1
    result1 = min(result1, count)
print(result1, result2)
'''


'''
<1차 시도>
1. 2차원 배열로 석순, 종유석 높이를 저장
2. 1<=i<=h까지 for로 반복하면서 장애물의 최솟값을 저장 (기존의 result와 현재 count를 비교하여 더 최솟값으로 갱신)
이분 탐색 방법으로 안풀고 2차원 배열로 장애물을 표현해서 각 높이마다 부셔야 하는 장애물 수를 구해서 최솟값 출력
=>메모리 초과
'''
'''
import sys

n,h=map(int,sys.stdin.readline().split())
cave=[[0]*n for _ in range(h)]
c=[]
for _ in range(n):
    c.append(int(input()))
for i in range(n):  #2차원 배열로 저장
    for j in range(h):
        if i%2!=0:  #종유석
            if c[i]-1>=j:
                cave[j][i]=1
        else:   #석순
            if h-j<=c[i]:
                cave[j][i]=1
result1=float('inf')    #개똥벌레가 파괴해야 하는 장애물 수
result2=1   #파괴해야 하는 장애물의 최솟값 구간의 수
for i in range(h,0,-1): #배열의 위부터 탐색
    count=0
    for j in range(n):
        if cave[i-1][j]==1:
            count+=1
    if result1==count:
        result2+=1
    result1=min(result1,count)
print(result1,result2)
'''