'''
- 이슈 검색어
    1) n일 동안 매일 k번 이상
    2) n일동안 총 2XnXk번 이상
- 최고 이슈 검색어
    이슈 검색어 중 가장 여러번 검색된 것
    여러개일 경우, 사전 순 정렬렬
- 최고 이슈 검색어 없으면 None 리턴

1. 각 요일마다 검색어 당 몇 번 나왔는지 count
2. 각각 검색어마다 이슈 검색어인지 확인
    이슈 검색어면 search 딕셔너리에 넣기 + 이슈 된 날 카운트
3. search 딕셔너리 사전 순 정렬
'''
from collections import Counter

def solution(research, n, k):
    s=set()
    for res in research:
        res=set(res)
        for r in res:
            s.add(r)

    countDic = {}
    for ss in s:
        countDic[ss]=[0]*len(research)

    for idx,r in enumerate(research):
        counter = Counter(r)
        for c in counter.items():
            countDic[c[0]][idx]+=c[1]
    #print("countDic:",countDic)

    issueDic ={}
    # 이슈 검색어인지 확인
    for key,value in countDic.items():
        #print("key,value : ",key,value)
        idx,cnt,count=0,0,0
        while idx<len(research)-1:
            #print("idx:",idx)
            for i in range(n):
                if value[idx+i]<k:
                    #print("idx+i:",idx+i)
                    break
            else:
                for i in range(idx,idx+n):
                    cnt+=value[i]
                    if cnt>=2*n*k: count+=1
                    #print("i, cnt, count : ",i,cnt,count)
            idx+=1
        if count:
            issueDic[key]=count
    print(issueDic)

    if issueDic:
        return sorted(issueDic.items(),key=lambda x:(-x[1],x[0]))[0][0]
    return "None"

#print(solution(["abaaaa","aaa","abaaaaaa","fzfffffffa"],2,2))
#print(solution(["yxxy","xxyyy"],2,1))
#print(solution(["yxxy","xxyyy","yz"],2,1))
print(solution(["xy","xy"],1,1))