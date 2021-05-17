#드래곤 앤 던전
'''
피해 입은 만큼 damage-
물약 회복 만큼 damage+
'''
import sys

n,atk=map(int,sys.stdin.readline().split())
info=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
maxHp,curHp,damage=0,0,0

for i in range(n):
    t,a,h=info[i]
    # 몬스터와 전투
    if t==1:
        temp=h%atk
        if temp==0: damage=-(a*(h//atk-1))
        else: damage=-(a*(h//atk))
    # 물약 마시기
    else:
        atk+=a
        damage=h

    curHp+=damage
    # 피해 받은 것보다 더 많이 회복 된 경우
    if curHp>0: curHp=0
    maxHp=max(maxHp,abs(curHp))
print(maxHp+1)