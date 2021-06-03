#Cubeditor
'''
KMP 문자열 검색 알고리즘
prefix, suffix가 일치하는 최대 길이 구함
시간 복잡도 O(N+M) (N:문자열 길이, M:비교 문자열 길이)
'''
import sys

def kmp(s):
    table=[0]*len(s)    # table[i] : i까지 중 일치하는 접두사, 접미사 패턴의 최대 길이 저장
    j=0     # j: prefix
    for i in range(1,len(s)):   # i: suffix
        while j>0 and s[i]!=s[j]:
            # 가장 최근에 매칭됐던 인덱스(j-1)의 값부터 다시 매칭 시작
            j=table[j-1]
        # prefix=suffix면 table에 패턴 길이 저장하고, 다음 문자로 넘어가기
        if s[i]==s[j]:
            j+=1
            table[i]=j
    return max(table)

string=sys.stdin.readline().strip()
result=0
for i in range(len(string)):
    # kmp 알고리즘은 문자열의 위치가 접미사, 접두사일 때만 해당
    # 이 문제에선 반복되는 문자열이 꼭 접미사, 접두사 위치가 아니여도 됨
    # 따라서 나올 수 있는 모든 문자열에 대해 fail 함수를 구해야 함
    s=string[i:len(string)]
    result=max(result,kmp(s))
print(result)