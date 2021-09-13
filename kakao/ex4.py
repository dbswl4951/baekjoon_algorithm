'''
- 어치피 n발 -> 라이언 n발
- k점을 어피치 a, 라이언 b발 맞춤
    1) a,b 중 더 큰게 k점 가져감
    2) a==b : 어피치가 k점 가져감
    3) a=b=0 : 점수 X
- 최종 점수가 같을 경우, 어치피 우승

라이언이 큰 점수차로 이기기 위해 n발로 어떻게 맞춰야 할지?
맞춰야 할 과녁 점수를 return

브루트포스
'''

# (20/25) 통과
import copy
score=0
result=[]

def dfs(k,remain,lion,apeach,r):
    global score,result

    if remain==0 or k==0:
        lionScore, apeachScore = 0, 0
        # 점수 차이 구하기
        for i in range(11):
            if apeach[i] < lion[i]:
                lionScore += (10 - i)
            elif apeach[i] > lion[i]:
                apeachScore += (10 - i)
        if score <= lionScore - apeachScore:
            if score==lionScore - apeachScore:
                r.append(lion)
            else:
                score = lionScore - apeachScore
                r=[]
                r.append(lion)
            result = copy.deepcopy(r)
        return

    for i in range(10-k,11):
        if apeach[i]<remain:
            remain-=apeach[i]+1
            l=lion[i]
            lion[i]=apeach[i]+1
            dfs(k-1,remain,lion,apeach,r)
            remain += apeach[i] + 1
            lion[i]=l

def solution(n, info):
    dfs(10,n,[0]*11,info,[])
    if result:
        result.sort()
        return result[0]
    return [-1]

#print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
#print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
#print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))


# (11/18) 정답
'''
def solution(n, info):
    score,idx = 0,0
    result =[]
    while idx<11:
        remain,tempList,tempScore = n,[0]*11,0
        for i in range(idx,11):
            if info[i]<remain:
                # 어치피보다 무조건 1개 더 쏘기
                remain-=(info[i]+1)
                tempScore+=10-i
                tempList[i]=info[i]+1
            if remain==0: break
        lionScore,apeachScore =0,0
        for i in range(11):
            if info[i]<tempList[i]:
                lionScore+=(10-i)
            elif info[i]>tempList[i]:
                apeachScore+=(10-i)
        if score<lionScore-apeachScore:
            score=lionScore-apeachScore
            result=tempList
        idx+=1
    if result: return result
    return [-1]
'''