#소수의 연속합
'''
1) 에라토스테네스의 체를 이용해 소수를 모두 구함
2) 투포인터를 이용해 소수의 합이 n이 되는 개수 구함
'''
import sys

# 에라토스테네스 체 사용해서 소수 구하기
def getSosu():
    sosu=[]
    isSosu=[1 for _ in range(n+1)]
    isSosu[0],isSosu[1]=0,0

    for i in range(2,n+1):
        if isSosu[i]:
            sosu.append(i)
            for j in range(i*i,n+1,i):
                isSosu[j]=0
    return sosu

n=int(sys.stdin.readline().strip())
sosu=getSosu()
start,end=0,0
result=0
while start<=end and end<len(sosu):
    if sum(sosu[start:end+1])<n:
        end+=1
    elif sum(sosu[start:end+1])>n:
        start+=1
    else:
        result+=1
        end+=1
print(result)