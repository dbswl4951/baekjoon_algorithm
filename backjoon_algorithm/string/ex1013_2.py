#Contact
import sys,re

t=int(sys.stdin.readline().strip())
pattern='(100+1+|01)+'
for _ in range(t):
    string=sys.stdin.readline().strip()
    result=re.fullmatch(pattern,string)
    if result==None: print('NO')
    else: print('YES')