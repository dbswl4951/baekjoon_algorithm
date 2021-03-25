#부분 문자열
'''
KMP 알고리즘
'''
import sys

# 자기 자신을 제외 한 동일한 Prefix와 Suffix 쌍의 최대 길이 테이블 구하기
def LPS(pattern):
    lps=[0 for _ in range(len(pattern))]
    j=0 # j : Prefix
    for i in range(1,len(pattern)): # i : Suffix
        while j>0 and pattern[i]!=pattern[j]:
            j=lps[j-1]
        if pattern[i]==pattern[j]:
            j+=1
            lps[i]=j
    return lps

def KMP(sequence,pattern):
    lps=LPS(pattern)
    j=0 # j : pattern idx
    for i in range(len(sequence)):  # i : sequence idx
        # 하나 이상 문자열이 매칭 됐으나, 다음 문자열 매칭 X 일 때
        while j>0 and sequence[i]!=pattern[j]:
            # 가장 마지막으로 매칭 성공했던 LPS[idx] 값 확인
            j=lps[j-1]
        # 문자열이랑 pattern이 매칭 되면
        if sequence[i]==pattern[j]:
            if j==len(pattern)-1:
                return True
            else:
                j+=1
    return False

sequence=sys.stdin.readline().strip()
pattern=sys.stdin.readline().strip()
if KMP(sequence,pattern): print(1)
else: print(0)