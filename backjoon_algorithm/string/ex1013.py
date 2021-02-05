#Contact
'''
어떻게 풀어야 하는지 감도 안와서 구글 검색
정규 표현식을 이용해 푸는 문제
'''
import re,sys

t=int(sys.stdin.readline().strip())
result=[]
for _ in range(t):
    sign=sys.stdin.readline().replace('\n','')
    #re.compile(정규식) : 정규식 객체(RegexObject)를 리턴
    reObject=re.compile('(100+1+|01)+')
    #fullmatch(패턴,문자열,플래그) : 문자열의 시작과 끝이 정확하게 패턴과 일치 할 때 반환
    m=reObject.fullmatch(sign)
    if m :result.append("YES")
    else: result.append("NO")
for r in result:
    print(r)