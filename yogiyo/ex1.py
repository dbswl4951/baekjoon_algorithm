'''
First
Last
Company : 소문자, . 포함X
같은 email이 있을 경우, @전에 숫자 추가 (2부터..)
'''
def solution(S, C):
    names=S.split('; ')
    nameList=[]
    for name in names:
        temp=name.split(' ')
        for i in range(len(temp)):
            temp[i]=temp[i].lower()
            if not temp[i].isalpha():
                string=''
                for t in temp[i]:
                    if t.isalpha(): string+=t
                temp[i]=string
        if len(temp[-1])>8: temp[-1]=temp[-1][:8]
        if len(temp)==3: nameList.append([temp[0],temp[2]])
        else: nameList.append(temp)

    C=C.lower()
    result=''
    dic={}
    for idx,name in enumerate(nameList):
        first,last=name
        email=first+'.'+last+'@'+C+'.com'
        if first+last in dic.keys():
            dic[first+last]+=1
            if idx!=len(nameList)-1:
                email=first+'.'+last+str(dic[first+last])+'@'+C+'.com; '
            else:
                email = first + '.' + last + str(dic[first+last])+ '@' + C + '.com'
        else:
            dic[first+last]=1
            email+='; '
        result+=email
    return result

print(solution('John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker', 'Example'))