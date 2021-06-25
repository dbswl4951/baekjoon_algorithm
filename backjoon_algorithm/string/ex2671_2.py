#잠수함 식별
import sys,re

string=sys.stdin.readline().strip()
pattern='(100+1+|01)+'
s=re.fullmatch(pattern,string)
if s==None: print('NOISE')
else: print('SUBMARINE')