#문자열 재정렬

alpaNum=input()
alpaList=[]
numSum=0
sortStr=''
number=['0','1','2','3','4','5','6','7','8','9']
for s in alpaNum:
    if s not in number:     #알파벳인 경우
        alpaList.append(s)
    else:
        numSum+=int(s)
alpaList.sort()
for i in alpaList:
    sortStr+=i
    
print(sortStr+str(numSum))
