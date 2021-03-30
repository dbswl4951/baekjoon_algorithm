#수 묶기
'''
1. -값과 0 minusList, 1이상인 값 plusList로 나눔
2. minusList sort()로 오름차순 정렬 => 2개씩 묶어서 곱함
 만약 홀수 개라서 값이 하나 남는다면
 맨 마지막 값을 maxSum에 더해 줌
3. plusList sort()로 내림차순 정렬
 2-1) 만약 1이 포함 되어 있다면 곱하지 않고 더함
 2-2) 1이 없다면 2개씩 묶어서 곱함
 만약 홀수 개라서 값이 한 개 남는다면 maxSum에 더하기
'''

n = int(input())
minusList=[]    #-값,0
plusList=[]     #+값
maxSum=0

for i in range(n):
    num = int(input())
    if num<1 :
        minusList.append(num)
    else:
        plusList.append(num)

minusList.sort()
plusList.sort(reverse=True)

for i in range(0,len(minusList)-1,2):
    maxSum+=minusList[i]*minusList[i+1]

if len(minusList)%2!=0: #홀수개면
    maxSum+=minusList[-1]   #맨 마지막 인자 더해줌

for i in range(0,len(plusList)-1,2):
    if plusList[i+1]==1:    #1이면 곱하는 것보다 더하는 것이 값이 더 크다
        maxSum+=plusList[i]
        maxSum+=plusList[i+1]
    else:
        maxSum+=plusList[i]*plusList[i+1]
if len(plusList)%2!=0:  #홀수개면
    maxSum+=plusList[-1]    #맨 마지막 인자 더해 줌

print(maxSum)