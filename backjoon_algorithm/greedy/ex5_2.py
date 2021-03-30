#숫자 카드 게임2
'''
문제집에 나와있는대로 더 간단한 방법
'''

import sys

n,m = map(int,input().split())
result=0

for i in range(n):
    cardList=list(map(int,sys.stdin.readline().split()))
    minNum = min(cardList)  #해당 행에서 가장 작은 수 구함
    result = max(result,minNum)     #result와 minNum값 중 더 큰 값을 구함
print(result)