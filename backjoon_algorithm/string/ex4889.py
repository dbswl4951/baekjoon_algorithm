#안정적인 문자열
import sys

idx=1
while True:
    string=sys.stdin.readline().strip()
    result=0
    if '-' in string: break

    if string:
        stack=[]
        # 올바른 괄호 제거
        for s in string:
            if stack and s=='}' and stack[-1]=='{':
                stack.pop()
            else:
                stack.append(s)
        while stack:
            s1=stack.pop()
            s2=stack.pop()
            if s1+s2=='}}' or s1+s2=='{{': result+=1
            else: result+=2
    print(idx,end='')
    print('.',result)
    idx+=1