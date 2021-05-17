import sys
n, atk = map(int, sys.stdin.readline().split())
dungeon=[[] for i in range(n)]
maxHP, curHP, damage = 0, 0, 0
for i in range(n):
    t, a, h = map(int, sys.stdin.readline().split())
    if t==1: # 몬스터방
        temp = h%atk
        if temp == 0:
            damage = -(a * (h // atk - 1))
        else:
            damage = -(a * (h // atk))
    else: # 포션방
        atk += a
        damage = h
        print("atk,damage:",atk,damage)
    curHP += damage
    print("curHp:",curHP)
    if curHP > 0:
        curHP = 0 # 풀피일 때 포션먹는 경우
        print("curHp 0-----")
    maxHP = max(maxHP, abs(curHP))
    print("maxHp:",maxHP)
print(maxHP+1)