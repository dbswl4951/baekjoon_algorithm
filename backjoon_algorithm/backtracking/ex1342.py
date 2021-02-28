#행운의 문자열
'''
1차 시도 : permutations 순열 사용 => 메모리 초과
풀이 보고 2차 시도 : 백트레킹 사용
'''
import sys

#pre: 그 전 선택 문자, idx : 횟수
def dfs(pre,cnt):
    global result
    if cnt==sLen:
        result+=1
        return
    for i in range(26):
        #그 전 선택문자와 현재 문자열이 같으면 pass
        if not alpha[i] or pre==i: continue
        alpha[i]-=1
        dfs(i,cnt+1)
        alpha[i]+=1

s=sys.stdin.readline().strip()
alpha=[0 for _ in range(26)]
#문자가 몇 개 있는지 저장
for c in s:
    #ord():문자 -> 아스키 코드 값
    alpha[ord(c)-ord('a')]+=1
result=0
setLen=len(set(s))
sLen=len(s)
#시간 초과 줄이기 위해
if setLen==10:
    print(3628800)
else:
    dfs(-1,0)
    print(result)