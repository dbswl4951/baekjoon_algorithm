#압축
import sys

string = sys.stdin.readline().strip()
stack=[]
length,num=0,0
for s in string:
    if s.isdigit():
        length+=1
        num=s
    elif s=='(':
        # [괄호 앞 숫자, 괄호 앞 숫자 뺀 문자 길이]
        stack.append([num,length-1])
        length=0
    else:
        sNum,sLen=stack.pop()
        length=(int(sNum)*length)+sLen
print(length)