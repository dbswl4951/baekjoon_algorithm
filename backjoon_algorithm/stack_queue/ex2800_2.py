#괄호 제거
import sys
from itertools import combinations

string=list(sys.stdin.readline().strip())
stack,idxList=[],[]
result=set()

for i,s in enumerate(string):
    if s=='(':
        string[i]=''
        stack.append(i)
    elif s==')':
        string[i] = ''
        idx=stack.pop()
        idxList.append([idx,i])

for i in range(len(idxList)):
    if i==0:
        result.add(''.join(string))
        continue
    for case in combinations(idxList,i):
        s=string[:]
        for start,end in case:
            s[start]='('
            s[end]=')'
        result.add(''.join(s))
result=sorted(list(result))
for r in result: print(r)



# 1차 시도
# 거의 모든 TC를 넣었는데 잘 나옴. But 틀렸습니다 나옴.. 뭐가 문제?
'''
import sys
from itertools import combinations

string=sys.stdin.readline().strip()
stack,idxList=[],[]
result=set()

for i,s in enumerate(string):
    if s=='(':
        stack.append(i)
    elif s==')':
        idx=stack.pop()
        idxList.append([idx,i])
idxList.sort()

for i in range(1,len(idxList)+1):
    for case in combinations(idxList,i):
        cnt=0
        ss=list(string)
        # 선택된 case index에 있는 괄호 제거
        for j in range(len(case)):
            ss.pop(case[j][0] - cnt)
            ss.pop(case[j][1] - cnt - 1)
            if j!=len(case)-1 and case[j][1]<case[j+1][0]:
                cnt+=j+1
            cnt+=1
        result.add(''.join(ss))
result=list(result)
result.sort()
for r in result: print(r)
'''