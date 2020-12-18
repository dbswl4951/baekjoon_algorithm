#숫자 카드 게임
'''
1. 이차원 list에 값을 담고, 각 행에서 제일 작은 수를 구한다
2. 작은 수들 중 가장 큰 수를 찾는다
'''

import sys

n,m = map(int,input().split())
cardList=[]
minList=[]
for i in range(n):
    cardList.append(list(map(int,sys.stdin.readline().split())))
for i in cardList:
    minList.append(min(i))  #행의 가장 작은 수를 넣음
print(max(minList))     #뽑은 작은 수 중 가장 큰 수를 출력