#암호 만들기
import sys,itertools

l,c=map(int,sys.stdin.readline().split())
alphabet=list(sys.stdin.readline().split())
must=['a','e','i','o','u']
allAlpha=list(itertools.combinations(alphabet,l))
result=[]
for alpha in allAlpha:
    a = ''
    count=0
    temp=[]
    for i in alpha:
        temp.append(i)
        if i in must:
            count+=1
    if count>=1 and l-count>=2:
        temp.sort()
        a=''.join(temp)
        result.append(a)
result.sort()
for r in result:
    print(r)