def solution(id_list, report, k):
    reportDic,reportCountDic={},{}
    for id in id_list:
        reportDic[id]=[]
        reportCountDic[id]=0

    for re in report:
        user = re.split(' ')
        if user[0] not in reportDic:
            reportDic[user[0]].append(user[1])
            reportCountDic[user[1]]+=1
        elif user[1] not in reportDic[user[0]]:
            reportDic[user[0]].append(user[1])
            reportCountDic[user[1]] += 1
    #print('reportDic: ',reportDic)
    #print('reportCountDic: ', reportCountDic)

    stopUser=[]
    for key,value in reportCountDic.items():
        if value>=k: stopUser.append(key)
    #print('stopUser:',stopUser)

    resultDic={}
    for key,value in reportDic.items():
        resultDic[key]=0
        for v in value:
            if v in stopUser:
                resultDic[key]+=1

    result=[]
    for id in id_list:
        result.append(resultDic[id])

    return result

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))