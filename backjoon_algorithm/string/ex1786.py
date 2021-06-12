#찾기
'''
KMP 알고리즘

문자열 'ABC ABCDAB ABCDABCDABDE'에서 'ABCDABD'를 찾는다고 하면

1) 첫 세 글자 ABC 일치
2) 이후 2번째부터~4번째부터 시작할 때는 첫판부터 OUT.
3) 5번째부터 7번째까지는 ABC가 전부 일치

정석적으로 보면 1번째 글자 체크 이후 5번째로 바로 스킵해야 함! ((1)->(3)으로)
이를 빠르게 찾기 위해서, 첫 문자열의 끝 부분과 이후에 확인해야만 하는 문자열이 중첩되므로,
pattern의 Prefix(접두사)와 Suffix(접미사)가 같은 경우를 찾아야 함!

1. pattern의 fail 테이블 생성
2. fail 테이블을 이용 해 string, pattern의 일치 문자열 찾기
'''

# 패턴의 prefix, suffix 중복 테이블 생성 (fail 테이블 생성)
def makeFailTable():
    table=[0]*len(pattern)    # fail 테이블
    j=0     # prefix
    for i in range(1,len(pattern)):    # i: prefix
        # prefix!=suffix면, 그 전까지 일치했던 정보를 담고있는 table[j-1]를 대입
        # ex) pattern=abadabak이면 table=[0,0,1,0,1,2,3,0]
        # j=3,i=7에서 'd'와 'k'가 다름 -> j = tb[2] = 1로 복귀
        # 즉, 다른 비교도 건너뛰고 ab ak에서 a는 이미 비교했다고 보고 b와 k를 비교 (j=1, i=7부터 다시 비교)
        while j>0 and pattern[i]!=pattern[j]:
            j=table[j-1]
        if pattern[i]==pattern[j]:
            j+=1
            table[i]=j
    return table

def kmp():
    j=0
    count=0
    findIdx=[]

    for i in range(len(string)):
        # 비교 중간에 틀린 경우
        while j>0 and string[i]!=pattern[j]:
            j=table[j-1]
        if string[i]==pattern[j]:
            j+=1
            # 일치하는 문자열 찾음
            if j==len(pattern):
                count+=1
                findIdx.append(i-len(pattern)+2)
                # 다음 일치 문자열 찾기 위해, 그 전에 일치했던 문자열 위치로 이동
                j=table[j-1]
    return count,findIdx

string=input()
pattern=input()
table=makeFailTable()
result1,result2=kmp()
print(result1)
print(*result2)