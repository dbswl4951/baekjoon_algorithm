#A->B
'''
처음에 DP로 풀이 실행 => 실패
풀이 보니 간단한 그리디 문제였음..
'''
import sys

a,b=map(int,sys.stdin.readline().split())
count=1
while True:
    if a==b: break
    elif a>b or (b%10!=1 and b%2!=0):
        count=-1
        break
    elif b%10==1:
        b//=10
        count+=1
    elif b%2==0:
        b//=2
        count+=1
print(count)