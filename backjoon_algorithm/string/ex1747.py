#소수&팰린드롬
'''
에라토스테네스의 체 사용.
소수를 찾고 그 수가 팰린드롬인지 확인.

소수 찾는 문제를 예전에 풀어봤으나 기억이 안나서 다시 찾아봤다.
'''
import sys,math

n=int(sys.stdin.readline().strip())
maxV=1000001
sosu=[1]*maxV
sosu[0],sosu[1]=0,0
#에라토스테네스의 체
for i in range(2,int(math.sqrt(maxV))+1):
    j=2
    if sosu[i]:  #sosu의 배수들은 모두 소수가 아니다
        while i*j<maxV:
            sosu[i*j]=0
            j+=1
result=0
#팰린드롬 수를 찾고, 그 수가 소수인지 판별
for i in range(n,maxV):
    if i==1: continue
    if str(i)==str(i)[::-1]:    #str(i)[::-1]: 뒤집은 수
        if sosu[i]:
            result=i
            break
if result==0: result=1003001
print(result)