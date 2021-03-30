#연산자 끼워넣기
'''
브루트포스 알고리즘
'''
import sys
from itertools import permutations

n=int(sys.stdin.readline().strip())
numbers=list(map(int,sys.stdin.readline().split()))
temp=list(map(int,sys.stdin.readline().split()))
operator=[]
for i in range(1,5):
    operator+=[i]*temp[i-1]
operatorSet=[]
for op in list(permutations(operator)):
    operatorSet.append(op)
operatorSet=list(set(operatorSet))  #중복 제거
INF=int(1e9)
maxVal,minVal=-INF,INF
for case in operatorSet:
    t=numbers[0]
    for i in range(n-1):
        if case[i]==1:  #+
            t+=numbers[i+1]
        elif case[i] == 2:  #-
            t-=numbers[i+1]
        elif case[i] == 3:  #x
            t*=numbers[i+1]
        elif case[i]==4:    #//
            if t<0: t=-(-t//numbers[i+1])   #양수로 바꾼 뒤 몫을 구하고 그 몫을 음수로 변경
            else: t//=numbers[i+1]
    if t<minVal: minVal=t
    if t>maxVal: maxVal=t
print(maxVal)
print(minVal)


#시간 초과 풀이
'''
n=int(sys.stdin.readline().strip())
numbers=list(map(int,sys.stdin.readline().split()))
temp=list(map(int,sys.stdin.readline().split()))
operator=[]
for i in range(4):
    num=temp[i]
    for j in range(num):
        if i==0:
            operator.append('+')
        elif i==1:
            operator.append('-')
        elif i==2:
            operator.append('*')
        else:
            operator.append('//')
nPr=list(set(permutations(operator,n-1)))
INF=int(1e9)
maxVal,minVal=-INF,INF
t=str(numbers[0])
for i in range(len(nPr)):
    for j in range(n-1):
        t+=(nPr[i][j]+str(numbers[j+1]))
        print(t)
        t=eval(t)
        if nPr[i][j]=='//' and t<0: t=t+1
        t=str(t)
        print(t)
    if int(t)>maxVal: maxVal=int(t)
    if int(t)<minVal: minVal=int(t)
    t=str(numbers[0])
print(maxVal)
print(minVal)
'''