#큰 수의 법칙
'''
M의 크기가 100억 이상일 때 ex4의 풀이는 시간 초과가 날 수 있음!
** 반복되는 수열 파악 **

반복되는 수열의 길이 ? k+1
1. m이 k+1로 나눠 떨이질 때 :
    m/(k+1) :수열이 반복되는 횟수
    m/(k+1) : 큰 수가 등장하는 횟수
2. m이 k+1로 나눠 떨어지지 않을 때도 고려:
    m을 l+1로 나눈 나머지만큼 가장 큰 수가 추가로 더해짐
    따라서 가장 큰 수가 등장하는 횟수 : m/(k+1)*k + m%(k+1)
'''

import sys

n,m,k = map(int,sys.stdin.readline().split())
list = list(map(int,sys.stdin.readline().split()))
list.sort(reverse=True)
bigCount=int(m/(k+1))*k+m%(k+1)     #큰 수가 더해지는 횟수
sum = bigCount*list[0]  #큰 숫자들의 합
count=m-bigCount
sum+=count*list[1]
print(sum)

