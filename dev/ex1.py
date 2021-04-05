def getNumber(result):
    if result==1 or result==0: return 6
    elif result==2: return 5
    elif result==3: return 4
    elif result==4: return 3
    elif result==5: return 2
    else: return 1

def solution(lottos, win_nums):
    sLottos=set(lottos)
    sWin=set(win_nums)
    inter=sLottos & sWin
    if sLottos==sWin:
        return [1,1]
    result1, result2 = len(inter), len(inter)
    idx=0
    while idx<len(lottos):
        if lottos[idx] in inter:
            lottos.pop(idx)
        else: idx+=1
    for i in range(len(lottos)):
        if lottos[i]==0:
            result1+=1
    result = [getNumber(result1),getNumber(result2)]
    return result

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))