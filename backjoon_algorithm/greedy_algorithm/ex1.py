#1이 뢸 때까지
'''
<핵심 아이디어>
주어진 n에 대하여 최대한 많이 나누기 수행
왜냐하면 ::: n 값을 줄일 때 2 이상의 수로 나누는 작업이 1을 빼는 것보다 훨씬 수를 많이 줄일 수 있기 때문
'''

import sys

n,k=map(int,sys.stdin.readline().split())
count=0

while n!=1:
    if n%k == 0:
        n=n/k
    else:
        n-=1
    count+=1
print(count)