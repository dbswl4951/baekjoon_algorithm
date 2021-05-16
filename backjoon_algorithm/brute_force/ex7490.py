#0 만들기
import sys,copy
from itertools import product

t=int(sys.stdin.readline().strip())
oper=['+','-',' ']
for _ in range(t):
    n=int(sys.stdin.readline().strip())
    result=[]
    string=''
    for i in range(1,n+1): string+=str(i)
    for case in product(oper,repeat=n-1):
        st=copy.deepcopy(string)
        for i in range(1,2*n-1,2):
            st=st[:i]+case[i//2]+st[i:]

        idx=0
        s=copy.deepcopy(st)
        while idx<len(s):
            if s[idx]==' ':
                s=s[:idx]+s[idx+1:]
            else: idx+=1
        r=eval(s)
        if r==0: result.append(st)
    if result:
        result.sort()
        for r in result:
            print(r)
        print()