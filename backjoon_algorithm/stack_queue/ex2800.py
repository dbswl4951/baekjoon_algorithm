#괄호 제거
from itertools import combinations

operation=[*input().strip()]
open,shut=[],[]
for i,oper in enumerate(operation):
    if oper=='(':
        operation[i]=''
        open.append(i)
    if oper==')':
        operation[i]=''
        shut.append([open.pop(),i])
s=set()
for i in range(len(shut)):
    if i==0:
        s.add(''.join(operation[:]))
        continue
    for j in combinations(shut,i):
        op=operation[:]
        for start,end in j:
            op[start]='('
            op[end]=')'
            s.add(''.join(op[:]))
s=sorted(s)
for i in s:
    print(i)