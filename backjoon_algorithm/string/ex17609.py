#회문
'''
1차 시도 : 슬라이딩 이용 => 시간 초과
풀이 보고 2차 시도 : 투 포인터 이용
'''
import sys

#####2차 시도
#유사 회문인지 체크
def secondCheck(word,left,right):
    while left<right:
        if word[left]==word[right]:
            left+=1
            right-=1
        else: return 0
    return 1

#회문인지 체크
def firstCheck(word):
    left,right=0,len(word)-1
    while left<=right:
        #left, right 문자가 같은 경우
        if word[left]==word[right]:
            left+=1
            right-=1
        #문자가 다른 경우, 유사 회문인지 검사
        else:
            #한 문자를 건너 뛰고 검사 => left나 right를 한 칸 건너 뛰고 검사
            check1=secondCheck(word,left+1,right)
            check2=secondCheck(word,left,right-1)
            if check1 or check2: return 1
            else: return 2
    return 0

t=int(sys.stdin.readline().strip())
words=list(sys.stdin.readline().strip() for _ in range(t))
for word in words:
    result=firstCheck(word)
    print(result)


#####1차 시도
'''
t=int(sys.stdin.readline().strip())
strList=list(sys.stdin.readline().strip() for _ in range(t))
result=[]
for i in range(t):
    #회문 인 경우
    if strList[i]==strList[i][::-1]: result.append(0)
    else:
        for j in range(len(strList[i])-1):
            temp=str(strList[i][0:j])+str(strList[i][j+1:])
            if temp==temp[::-1]:
                result.append(1)
                break
        else: result.append(2)
for r in result:
    print(r)
'''