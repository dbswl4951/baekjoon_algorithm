'''
번호가 작은 자동차부터 차량 별 누적 요금 구하기

- 누적 시간 <= 기본 시간 : 기본 요금
- 누적 시간 > 기본 시간 :
    초과한 시간에서 단위 시간마다 단위 요금 +
    단위 시간으로 나눠 떨어지지 X => 올림
'''
import math

def solution(fees, records):
    inDic, outDic = {}, {}

    for record in records:
        temp = record.split(' ')
        time,num,inout = temp
        if inout == 'IN':
            inDic[num] = time
        else:
            inTime = inDic.pop(num)
            # 주차 시간 계산
            hour,minute = inTime[:2],inTime[3:]
            inTime = int(hour)*60 + int(minute)
            hour,minute = time[:2],time[3:]
            outTime = int(hour)*60 + int(minute)
            # outDic에 넣기 (총 주차 되어있던 시간)
            if num in outDic:
                outDic[num]+=outTime-inTime
            else:
                outDic[num]=outTime-inTime

    # 23:59에 출차 된 차 더하기
    outTime = 23*60 + 59
    for key,value in inDic.items():
        hour, minute = value[:2], value[3:]
        inTime = int(hour) * 60 + int(minute)
        if key in outDic: outDic[key]+= outTime-inTime
        else: outDic[key]=outTime-inTime
    #print(outDic)

    resultDic={}
    # 주차 요금 구하기
    for key,value in outDic.items():
        #print("key,value : ",key,value)
        resultDic[key]=fees[1]
        if value>fees[0]:
            delayTime = value-fees[0]
            #print("delayTime:",delayTime)
            resultDic[key] += math.ceil(delayTime/fees[2])*fees[3]
        #print("Result : ",result)

    #print(resultDic)
    resultList = list(sorted(resultDic.items()))
    #print(resultList)
    result=[]
    for rl in resultList: result.append(rl[1])
    return result


print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10],["00:00 1234 IN"]))