#거짓말
'''
1. 모든 증인 구하기
2. 모든 파티 검사하면서 증인이 있는지 체크
'''
import sys

n,m=map(int,sys.stdin.readline().split())
witness=list(map(int,sys.stdin.readline().split()))[1:]
witness=set(witness)
party=[]

for i in range(m):
    person=list(map(int,sys.stdin.readline().split()))[1:]
    # 공통 부분 집합이 있다면 witness에 추가 (isdisjoint():서로소 집합인지 판단)
    if not witness.isdisjoint(set(person)):
        witness=witness.union(set(person))
    party.append(person)
# 모든 파티 돌면서 증인 구해서 witness에 넣기
for _ in range(m):
    for i in range(m):
        if not witness.isdisjoint(set(party[i])):
            witness=witness.union(set(party[i]))

result=0
for p in party:
    if witness.isdisjoint(set(p)): result+=1
print(result)