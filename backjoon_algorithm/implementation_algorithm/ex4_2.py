#문자열 재정렬

alpaNum=input()
alpaList=[]
numSum=0
sortStr=''

for s in alpaNum:
    if s.isalpha():  #isalpha(): 문자열인지 아닌지 판별. 숫자나 공백이 섞여있으면 false 리턴
        alpaList.append(s)
    else:
        numSum += int(s)
alpaList.sort()
for i in alpaList:
    sortStr += i

print(sortStr + str(numSum))
