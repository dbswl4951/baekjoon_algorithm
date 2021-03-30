#큰 수의 법칙
'''
1. list 내림차순 정렬
2. 큰 수 a,b를 고름
3. K씩 번갈아가면서 sum에 더함
    만약 m번만큼 더 했으면 종료 후 출력
'''
import sys

n,m,k = map(int,sys.stdin.readline().split())
list = list(map(int,sys.stdin.readline().split()))
list.sort(reverse=True)
num1,num2=list[0],list[1]
sum=0
i=0

while i<m:
    for _ in range(k):
        if i<m:
            sum+=num1
            i+=1
    if i<m:
        sum+=num2
        i+=1
print(sum)