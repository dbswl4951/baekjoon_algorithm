'''
sticky == True
같은 수의 task
'''
def solution(servers, sticky, requests):
    result = [[] for _ in range(servers)]
    if not sticky:
        sIdx,rIdx=0,0
        while rIdx<len(requests):
            result[sIdx].append(requests[rIdx])
            sIdx+=1
            rIdx+=1
            if sIdx>=servers: sIdx=0
    else:
        sIdx, rIdx,remember = 0, 0,requests[0]
        while rIdx<len(requests):
            if rIdx==0:
                result[0].append(requests[0])
                sIdx+=1
            elif remember==requests[rIdx]:
                result[sIdx-1].append(requests[rIdx])
            else:
                remember=requests[rIdx]
                result[sIdx].append(requests[rIdx])
                sIdx+=1
            rIdx += 1
            if sIdx>=servers: sIdx=0
    return result

#solution(2,1,[1,2,2,3,4,1])
#solution(2,0,[1,2,3,4])
#solution(5,1,[1,3,1,3,1,3,1])
print(solution(3,1,[1,2,4,4,4]))