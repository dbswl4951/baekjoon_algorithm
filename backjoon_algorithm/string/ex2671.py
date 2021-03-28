#잠수함 식별
'''
정규식 사용
'''
import sys,re

s=sys.stdin.readline().strip()
# ab+:b가 1개 이상 반복, ab|c:ab OR c
pattern=re.compile('(100+1+|01)+')
# match() : 패턴이 일치되는 것이 있는지를 확인 (문자열에 패턴이 있기만 하면 정규식 객체 반환)
# fullmatch() : 패턴과 문자열이 남는 부분 없이 완벽하게 일치하는지를 검사
m=pattern.fullmatch(s)
if m==None: print('NOISE')
else: print('SUBMARINE')